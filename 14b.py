def knotHash(inputString):
    lengthList = []

    for length in inputString.rstrip():
        lengthList.append(ord(length))

    for endLength in [17, 31, 73, 47, 23]:
        lengthList.append(endLength)

    stdList = []
    for i in range(0,256):
        stdList.append(i)

    currentPosition = 0
    skipSize = 0

    for j in range(0, 64):
        for length in lengthList:
            sublist = []

            pos = currentPosition
            i = 0
            while i < length:
                sublist.append(stdList[pos])
                if pos >= len(stdList) - 1:
                    pos = 0
                else:
                    pos += 1
                i += 1

            sublist.reverse()
            pos = currentPosition
            i = 0
            while i < length:
                stdList[pos] = sublist[i]
                if pos >= len(stdList) - 1:
                    pos = 0
                else:
                    pos += 1
                i += 1

            currentPosition += length + skipSize
            while currentPosition > len(stdList) - 1:
                currentPosition = currentPosition - len(stdList)
            skipSize += 1

    stringRepresentation = ""

    k = 0
    while k < len(stdList):
        xor = stdList[k]
        for i in range(1, 16):
            xor = xor ^ stdList[k + i]
        k += 16

        stringRepresentation += format(xor, '0>2x')

    binString = ""

    binString = format(int(stringRepresentation, 16), '0>128b')

    return binString

f = open("14input.txt")

hashInput = f.readlines()[0].rstrip()

hashes = []

for i in range(0,128):
    hashes.append(knotHash(hashInput + "-" + str(i)))

checked = [[False for x in range(128)] for y in range(128)]
groups = [["." for x in range(128)] for y in range(128)]

squaresStack = []
numGroups = 0

for i in range(0,128):
    for j in range(0,128):
        if checked[i][j]:
            continue
        if hashes[i][j] == "1":
            numGroups += 1
            squaresStack.append([i, j])
        else:
            checked[i][j] = True

        while len(squaresStack) != 0:
            currentChecker = squaresStack.pop()
            checked[currentChecker[0]][currentChecker[1]] = True
            if hashes[currentChecker[0]][currentChecker[1]] == "0":
                continue
            groups[currentChecker[0]][currentChecker[1]] = str(numGroups)

            if currentChecker[0] != 0:
                if not(checked[currentChecker[0] - 1][currentChecker[1]]):
                    squaresStack.append([currentChecker[0] - 1, currentChecker[1]])
            if currentChecker[0] != 127:
                if not(checked[currentChecker[0] + 1][currentChecker[1]]):
                    squaresStack.append([currentChecker[0] + 1, currentChecker[1]])
            if currentChecker[1] != 0:
                if not(checked[currentChecker[0]][currentChecker[1] - 1]):
                    squaresStack.append([currentChecker[0], currentChecker[1] - 1])
            if currentChecker[1] != 127:
                if not(checked[currentChecker[0]][currentChecker[1] + 1]):
                    squaresStack.append([currentChecker[0], currentChecker[1] + 1])

print(numGroups)
