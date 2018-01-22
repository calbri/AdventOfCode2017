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

waiting0 = False
waiting1 = False

counter0 = 0
counter1 = 0

values0 = []
values1 = []

registers0 = {}
registers1 = {}

for i in range(ord('a'), ord('z') + 1):
    registers0[chr(i)] = 0
    registers1[chr(i)] = 0

registers0['p'] = 0
registers1['p'] = 1

numSends1 = 0

while True:
    if not(waiting0):
        inst = instructions[counter0]
        firstArg = 0
        secondArg = 0

        if inst[0] != "set":
            if inst[1].isalpha():
                firstArg = registers0[inst[1]]
            else:
                firstArg = int(inst[1])

        if len(inst) > 2:
            if inst[2].isalpha():
                secondArg = registers0[inst[2]]
            else:
                secondArg = int(inst[2])

        if inst[0] == "snd":
            values1.append(firstArg)
        elif inst[0] == "set":
            registers0[inst[1]] = secondArg
        elif inst[0] == "add":
            registers0[inst[1]] += secondArg
        elif inst[0] == "mul":
            registers0[inst[1]] *= secondArg
        elif inst[0] == "mod":
            registers0[inst[1]] %= secondArg
        elif inst[0] == "rcv":
            if len(values0) != 0:
                registers0[inst[1]] = values0.pop(0)
            else:
                waiting0 = True
                counter0 -= 1
        elif inst[0] == "jgz":
            if firstArg > 0:
                counter0 += secondArg - 1

        counter0 += 1
    else:
        inst = instructions[counter0]
        firstArg = 0
        secondArg = 0

        if inst[0] != "set":
            if inst[1].isalpha():
                firstArg = registers0[inst[1]]
            else:
                firstArg = int(inst[1])

        if len(inst) > 2:
            if inst[2].isalpha():
                secondArg = registers0[inst[2]]
            else:
                secondArg = int(inst[2])

        if len(values0) != 0:
            registers0[inst[1]] = values0.pop(0)
            waiting0 = False
            counter0 += 1

    if not(waiting1):
        inst = instructions[counter1]
        firstArg = 0
        secondArg = 0

        if inst[0] != "set":
            if inst[1].isalpha():
                firstArg = registers1[inst[1]]
            else:
                firstArg = int(inst[1])

        if len(inst) > 2:
            if inst[2].isalpha():
                secondArg = registers1[inst[2]]
            else:
                secondArg = int(inst[2])

        if inst[0] == "snd":
            values0.append(firstArg)
            numSends1 += 1
        elif inst[0] == "set":
            registers1[inst[1]] = secondArg
        elif inst[0] == "add":
            registers1[inst[1]] += secondArg
        elif inst[0] == "mul":
            registers1[inst[1]] *= secondArg
        elif inst[0] == "mod":
            registers1[inst[1]] %= secondArg
        elif inst[0] == "rcv":
            if len(values1) != 0:
                registers1[inst[1]] = values1.pop(0)
            else:
                waiting1 = True
                counter1 -= 1
        elif inst[0] == "jgz":
            if firstArg > 0:
                counter1 += secondArg - 1

        counter1 += 1
    else:
        inst = instructions[counter1]
        firstArg = 0
        secondArg = 0

        if inst[0] != "set":
            if inst[1].isalpha():
                firstArg = registers1[inst[1]]
            else:
                firstArg = int(inst[1])

        if len(inst) > 2:
            if inst[2].isalpha():
                secondArg = registers1[inst[2]]
            else:
                secondArg = int(inst[2])

        if len(values1) != 0:
            registers1[inst[1]] = values1.pop(0)
            waiting1 = False
            counter1 += 1

    if (waiting0 and waiting1 and len(values0) == 0 and len(values1) == 0):
        break

print(numSends1)
