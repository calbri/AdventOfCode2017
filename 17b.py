f = open("17input.txt")

steps = int(f.readlines()[0].rstrip())

after0 = 0

size = 1
currentPos = 0
currentVal  = 1

loop = 50000000

for i in range(0,loop):
    currentPos = (currentPos + steps) % size

    if currentPos == 0:
        after0 = currentVal

    currentVal += 1
    size += 1
    currentPos += 1

print(after0)
