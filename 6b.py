f = open("6input.txt")

memory = f.readlines()[0]

currentMem = []
for num in memory.split("\t"):
    currentMem.append(int(num))

visitedMem = []
visitedMem.append(currentMem)

numIterations = 0
while True:
    numIterations += 1
    nextMem = []

    maxAmount = 0
    maxIndex = -1
    for num, amount in enumerate(currentMem):
        if amount > maxAmount:
            maxIndex = num
            maxAmount = amount

    amountLeft = maxAmount
    index = maxIndex
    currentMem[index] = 0

    nextMem = currentMem[:]

    while amountLeft > 0:
        if (index == len(currentMem) - 1):
            index = 0
        else:
            index += 1

        nextMem[index] += 1
        amountLeft -= 1

    if nextMem in visitedMem:
        # print(nextMem)
        # print(visitedMem)
        for num, mem in enumerate(visitedMem):
            if mem == nextMem:
                print(numIterations - num)
        break

    visitedMem.append(nextMem)

    currentMem = nextMem[:]
    # print(currentMem)
