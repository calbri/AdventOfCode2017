numPrograms = 16

programs = [0 for x in range(0, numPrograms)]

i = 0
for p in range(ord('a'), ord('p') + 1):
    programs[i] = p
    i += 1

oldProg = programs[:]

f = open("16input.txt")

moves = f.readlines()[0].split(",")

instructions = []

loop = 1000000000

for move in moves:
    if move[0] == "s":
        numMoves = int(move.rstrip()[1:])

        inst = ['s', numMoves]
        instructions.append(inst)

    elif move[0] == "x":
        exchange = move.rstrip()[1:]
        first = int(exchange.split("/")[0])
        second = int(exchange.split("/")[1])

        inst = ['x', [first, second]]
        instructions.append(inst)

    elif move[0] == "p":
        exchange = move.rstrip()[1:]
        firstProg = ord(exchange.split("/")[0])
        secondProg = ord(exchange.split("/")[1])

        inst = ['p', [firstProg, secondProg]]
        instructions.append(inst)

i = 0
while i < loop:
    for inst in instructions:
        if inst[0] == "s":
            numMoves = inst[1]

            newPrograms = [0 for x in range(0, numPrograms)]

            for j in range(0, numPrograms):
                pos = (j + numMoves) % 16
                newPrograms[pos] = programs[j]

            programs = newPrograms[:]

        elif inst[0] == "x":
            first = inst[1][0]
            second = inst[1][1]

            firstProg = programs[first]
            secondProg = programs[second]

            programs[first] = secondProg
            programs[second] = firstProg

        elif inst[0] == "p":
            firstProg = inst[1][0]
            secondProg = inst[1][1]

            firstPos = programs.index(firstProg)
            secondPos = programs.index(secondProg)

            programs[firstPos] = secondProg
            programs[secondPos] = firstProg

    if programs == oldProg:
        cycle = i + 1
        while i < loop:
            i += cycle
        i -= cycle

    i += 1

endString = ""

for p in programs:
    endString += chr(p)

print(endString)
