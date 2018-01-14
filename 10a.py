lengthList = []
f = open("10input.txt")
for length in f.readlines()[0].split(","):
    lengthList.append(int(length.rstrip()))

stdList = []
for i in range(0,256):
    stdList.append(i)

currentPosition = 0
skipSize = 0

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
    if currentPosition > len(stdList) - 1:
        currentPosition = currentPosition - len(stdList)
    skipSize += 1

print(stdList[0] * stdList[1])
