inputNum = 265149
locations = {}

location = 1
numSteps = 1
lastSteps = 0
horizontal = True
numStepsRight = 0
numStepsUp = 0
right = True
up = True

locations[(0,0)] = 1

i = 0

while (i < inputNum):
    i += 1
    total = 0

    if (horizontal):
        if (right):
            numStepsRight += 1
        else:
            numStepsRight -= 1
    else:
        if (up):
            numStepsUp += 1
        else:
            numStepsUp -= 1

    for key in locations:
        for i in (-1,0,1):
            for j in (-1,0,1):
                if (i == j == 0):
                    continue
                if (key == (numStepsRight+i, numStepsUp+j)):
                    total += locations[key]

    locations[(numStepsRight, numStepsUp)] = total

    if (total > inputNum):
        print (total)
        break

    lastSteps += 1

    if (lastSteps == numSteps):
        if (horizontal):
            right = not(right)
        else:
            up = not(up)
            numSteps += 1
        horizontal = not(horizontal)
        lastSteps = 0
