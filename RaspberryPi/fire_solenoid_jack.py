top = 0
bottom = 1

for i in range(5):
    close_all()
    two.open(top)
    six.open(top)
    five.open(bottom)
    three.open(bottom)

    sleep(3)

    close_all()
    two.open(bottom)
    six.open(bottom)
    five.open(top)
    three.open(top)
    sleep(3)

close_all()
