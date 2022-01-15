from time import sleep
import subprocess
from subprocess import Popen
import requests
import os
import io
import urllib.request
import time
import asyncio
from datetime import datetime

# Config options
baseURL = "http://localhost/"
cycleURL = baseURL + "queue/cycle"
getCurrentQueueURL = baseURL + "queue/current"
logURL = baseURL + "log"

file = "file.py" # original file download location
fileClean = "fileClean.py" # cleaned up file location
delete_list = ["<pre>", "</pre>"] # things to remove from files from the website
sleepTime = 2 # seconds

# Process Vars
lastRunTime = 0
lastProcess = None
maxProcessTime = 60 # seconds

def custom_print(msg):
    date_time = datetime.now().strftime("[%m/%d/%Y, %H:%M:%S]")
    print(date_time + " " + msg)
    log(msg)

def log(msg):
    requests.post(logURL, data = {"message": msg})

async def EasyControlLoop():
    while True:
        try:
            # Making a get request
            response = requests.get(getCurrentQueueURL)
            
            # Download currrent queue item.
            urllib.request.urlretrieve(getCurrentQueueURL, file)

            with open(file) as fin, open(fileClean, "w+") as fout:
                for line in fin:
                    for word in delete_list:
                        line = line.replace(word, "")
                    fout.write(line)
                    
            os.remove(file)

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
            lastProcess = Popen(['python', fileClean], stdout = subprocess.PIPE)
            lastRunTime = time.time()
            poll = None

            custom_print("Running process...")
            while (poll is None and (time.time() - lastRunTime) < maxProcessTime):
                poll = lastProcess.poll()
                await asyncio.sleep(1)

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