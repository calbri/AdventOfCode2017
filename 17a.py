f = open("17input.txt")

steps = int(f.readlines()[0].rstrip())

buff = [0]

size = 1
currentPos = 0
currentVal  = 1

for i in range(0,2017):
    for j in range(0,steps):
        currentPos = (currentPos + 1) % size

    buff.insert(currentPos + 1, currentVal)

    currentVal += 1
    size += 1
    currentPos += 1



for i in range(0, len(buff)):
    if buff[i] == 2017:
        print(buff[i + 1])
        break
