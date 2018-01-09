square = 265149

location = 1
numSteps = 1
lastSteps = 0
horizontal = True
numStepsRight = 0
numStepsUp = 0
right = True
up = True

while (location != square):
    location += 1
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
    lastSteps += 1

    if (lastSteps == numSteps):
        if (horizontal):
            right = not(right)
        else:
            up = not(up)
            numSteps += 1
        horizontal = not(horizontal)
        lastSteps = 0

print(abs(numStepsRight)+abs(numStepsUp))
