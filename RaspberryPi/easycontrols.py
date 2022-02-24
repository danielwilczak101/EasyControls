from subprocess import Popen, PIPE
import requests
import os
import urllib.request
import time
import asyncio
from datetime import datetime

# Config options
baseURL = "http://easycontrols.org/"
cycleURL = baseURL + "queue/cycle"
getCurrentQueueURL = baseURL + "queue/current"
logURL = baseURL + "log"

file = "file.py" # original file download location
fileClean = "fileClean.py" # cleaned up file location
delete_list = ["<pre>", "</pre>"] # things to remove from files from the website
sleepTime = 2 # seconds

# Process Vars
lastRunTime = 0 # unix epoch time
lastProcess = None
maxProcessTime = 60 # seconds
processCheckFrequency = 10 # hertz

def custom_print(msg):
    date_time = datetime.now().strftime("[%m/%d/%Y, %H:%M:%S]")
    print(date_time + " " + msg)
    log(msg)

def log(msg):
    requests.post(logURL, data = {"message": msg, "key": "fuckoff"})

def remove_words_from_file(file:str,delete_list:list[str],fileClean:str):
    """
    Removes words specified in delete_list from file and
    saves as new fileClean name.

    Example:
        >>> remove_words_from_file("oldfile.py",["<pre>","</pre>"],"newfile.py")
        Removes all instances of <pre> and </pre> from oldfile.py and
        saves it as newfile.py

    Args:
        file: Name of file that is to be cleaned.
        delete_list: List of words to be removed.
        fileClean: Name of file to be assiigned after cleaning.

    Returns:
        File that has been cleaned with given name.
    """
    with open(file) as fin, open(fileClean, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)

    os.remove(file)

async def EasyControlLoop():
    while True:
        try:
            # Making a get request
            response = requests.get(getCurrentQueueURL)
            
            # Download currrent queue item.
            urllib.request.urlretrieve(getCurrentQueueURL, file)

            # Removes words not wanted in the file.
            remove_words_from_file(file,delete_list,fileClean)
                    
            contents = open(fileClean).read()
            if (contents == "nothing in queue"):
                custom_print("Nothing in queue")
                os.remove(fileClean)
                await asyncio.sleep(sleepTime)
                continue

            # TODO: security checks, make sure this isnt going to brick anything
            # check for things like operating system calls, etc.
            # maybe a blacklist of certain packages and functions

            # Run File
            try:
                lastProcess = Popen(['python', fileClean], stdout=PIPE)
                lastRunTime = time.time()
                poll = None

                custom_print("Running process...")
                while (poll is None and (time.time() - lastRunTime) < maxProcessTime):
                    # Log subprocess terminal output
                    custom_print(lastProcess.stdout.readline().rstrip().decode())

                    poll = lastProcess.poll()
                    await asyncio.sleep(1/processCheckFrequency)
            except Exception as e:
                custom_print("Error while running process: " + e)

            lastProcess.kill()
            custom_print("Process killed")

            # Once finished, remove file.
            os.remove(fileClean)
        except KeyboardInterrupt:
            custom_print("Operation Cancelled")
        except:
            custom_print("error")

        requests.get(cycleURL)
        await asyncio.sleep(sleepTime) 

if __name__ == '__main__':
    custom_print("EasyControls Server Online")
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(EasyControlLoop())
        loop.run_forever()
    except KeyboardInterrupt:
        custom_print("Exiting")