f = open("18input.txt")

instructions = []

for inst in f.readlines():
    instruction = inst.split(" ")[0]

    if len(inst.split(" ")) == 3:
        arg1 = inst.split(" ")[1].rstrip()
        arg2 = inst.split(" ")[2].rstrip()

        instructions.append([instruction, arg1, arg2])
    else:
        arg1 = inst.split(" ")[1].rstrip()
        instructions.append([instruction, arg1])

recovered = False
soundFreq = 0
counter = 0

registers = {}

for i in range(ord('a'), ord('z') + 1):
    registers[chr(i)] = 0

while not(recovered):
    inst = instructions[counter]
    firstArg = 0
    secondArg = 0

    if inst[0] != "set":
        if inst[1].isalpha():
            firstArg = registers[inst[1]]
        else:
            firstArg = int(inst[1])

    if len(inst) > 2:
        if inst[2].isalpha():
            secondArg = registers[inst[2]]
        else:
            secondArg = int(inst[2])

    if inst[0] == "snd":
        soundFreq = firstArg
    elif inst[0] == "set":
        registers[inst[1]] = secondArg
    elif inst[0] == "add":
        registers[inst[1]] += secondArg
    elif inst[0] == "mul":
        registers[inst[1]] *= secondArg
    elif inst[0] == "mod":
        registers[inst[1]] %= secondArg
    elif inst[0] == "rcv":
        if firstArg != 0:
            recovered = True
    elif inst[0] == "jgz":
        if firstArg > 0:
            counter += secondArg - 1

    counter += 1

print(soundFreq)
