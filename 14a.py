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

numUsedSquares = 0

for i in range(0,128):
    for char in knotHash(hashInput + "-" + str(i)):
        if char == "1":
            numUsedSquares += 1

print(numUsedSquares)
