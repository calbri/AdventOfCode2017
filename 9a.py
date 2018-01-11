f = open("9input.txt")
groupString = f.readlines()[0]

groupLevel = 0
garbage = False
totalScore = 0

numChars = len(groupString)
charNum = 0

while True:
    if charNum >= numChars:
        break
    char = groupString[charNum]
    if char == '!':
        charNum += 2
        continue
    elif char == '<':
        garbage = True
    elif char == '>':
        garbage = False

    if not(garbage):
        if char == '{':
            groupLevel += 1
        elif char == '}':
            totalScore += groupLevel
            groupLevel -= 1

    charNum += 1

print(totalScore)
