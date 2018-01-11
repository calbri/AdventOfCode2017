f = open("8input.txt")

registers = []
values = {}

for instruction in f.readlines():
    reg = instruction.split(" ")[0]

    if reg not in registers:
        values[reg] = 0
        registers.append(reg)

    regToCheck = instruction.split(" ")[4]

    if regToCheck not in registers:
        values[regToCheck] = 0
        registers.append(regToCheck)

    attribute = instruction.split(" ")[5]
    valueToCheck = int(instruction.split(" ")[6].rstrip())

    attributeValid = False

    if attribute == ">":
        if values[regToCheck] > valueToCheck:
            attributeValid = True
    elif attribute == ">=":
        if values[regToCheck] >= valueToCheck:
            attributeValid = True
    elif attribute == "<":
        if values[regToCheck] < valueToCheck:
            attributeValid = True
    elif attribute == "<=":
        if values[regToCheck] <= valueToCheck:
            attributeValid = True
    elif attribute == "==":
        if values[regToCheck] == valueToCheck:
            attributeValid = True
    elif attribute == "!=":
        if values[regToCheck] != valueToCheck:
            attributeValid = True

    if not(attributeValid):
        continue

    inst = instruction.split(" ")[1]
    val = int(instruction.split(" ")[2])

    if inst == "inc":
        values[reg] += val
    else:
        values[reg] -= val

maxVal = None

for reg in values:
    if maxVal == None:
        maxVal = values[reg]
    elif values[reg] > maxVal:
        maxVal = values[reg]

print(maxVal)
