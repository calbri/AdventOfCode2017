f = open("23input.txt")

instructions = []

for inst in f.readlines():
    instruction = inst.split(" ")[0]

    arg1 = inst.split(" ")[1].rstrip()
    arg2 = inst.split(" ")[2].rstrip()

    instructions.append([instruction, arg1, arg2])

registers = {}

for i in range(ord('a'), ord('h') + 1):
    registers[chr(i)] = 0

registers['a'] = 1

i = 0

while i < len(instructions):
    inst = instructions[i]
    firstArg = 0
    secondArg = 0

    if inst[1].isalpha():
        firstArg = registers[inst[1]]
    else:
        firstArg = int(inst[1])

    if inst[2].isalpha():
        secondArg = registers[inst[2]]
    else:
        secondArg = int(inst[2])

    if inst[0] == "set":
        registers[inst[1]] = secondArg
    elif inst[0] == "mul":
        registers[inst[1]] *= secondArg
    elif inst[0] == "sub":
        registers[inst[1]] -= secondArg
    elif inst[0] == "jnz":
        if firstArg != 0:
            i += secondArg - 1

    i += 1
    print(registers['h'])

print(registers['h'])
