from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

f = open("19input.txt")

puzzle = []

for line in f.readlines():
    puzzleLine = []
    for c in line:
        if c == "\n":
            continue
        puzzleLine.append(c)

    puzzle.append(puzzleLine)

currentPosition = [0,0]

j = 0
for c in puzzle[0]:
    if c == "|":
        currentPosition[1] = j
    j += 1

direction = Direction.DOWN

visited = ""

stepCount = 0

while True:
    stepCount += 1
    newPosition = currentPosition[:]

    if direction == Direction.DOWN:
        newPosition[0] += 1
    elif direction == Direction.UP:
        newPosition[0] -= 1
    elif direction == Direction.LEFT:
        newPosition[1] -= 1
    elif direction == Direction.RIGHT:
        newPosition[1] += 1



    newLocation = puzzle[newPosition[0]][newPosition[1]]

    if newLocation == "+":
        if direction == Direction.DOWN or direction == Direction.UP:
            if not(newPosition[1] == 0):
                if puzzle[newPosition[0]][newPosition[1] - 1] == "-" or puzzle[newPosition[0]][newPosition[1] - 1].isalpha():
                    currentPosition = [newPosition[0], newPosition[1] - 1]
                    direction = Direction.LEFT
            if not(newPosition[1] == len(puzzle[0]) - 1):
                if puzzle[newPosition[0]][newPosition[1] + 1] == "-" or puzzle[newPosition[0]][newPosition[1] + 1].isalpha():
                    currentPosition = [newPosition[0], newPosition[1] + 1]
                    direction = Direction.RIGHT
        else:
            if not(newPosition[0] == 0):
                if puzzle[newPosition[0] - 1][newPosition[1]] == "|" or puzzle[newPosition[0] - 1][newPosition[1]].isalpha():
                    currentPosition = [newPosition[0] - 1, newPosition[1]]
                    direction = Direction.UP
            if not(newPosition[0] == len(puzzle) - 1):
                if puzzle[newPosition[0] + 1][newPosition[1]] == "|" or puzzle[newPosition[0] + 1][newPosition[1]].isalpha():
                    currentPosition = [newPosition[0] + 1, newPosition[1]]
                    direction = Direction.DOWN
        stepCount += 1

    else:
        currentPosition = newPosition[:]

        if puzzle[currentPosition[0]][currentPosition[1]] == " ":
            break

    if puzzle[currentPosition[0]][currentPosition[1]].isalpha():
        visited += puzzle[currentPosition[0]][currentPosition[1]]


print(stepCount)
