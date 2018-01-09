f = open("5input.txt")
instructions = []

i = 0
for instruction in f.readlines():
    instructions.append(int(instruction))
    i += 1

currentPosition = 0
lastPosition = 0

numJumps = 0

while True:
    lastPosition = currentPosition

    if (lastPosition < 0) or (lastPosition > i - 1):
        break

    currentPosition = lastPosition + instructions[lastPosition]
    instructions[lastPosition] += 1

    numJumps += 1

print(numJumps)
