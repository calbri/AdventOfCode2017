f = open("15input.txt")

genA = int(f.readline().split(" ")[-1].rstrip())
genB = int(f.readline().split(" ")[-1].rstrip())

genAFactor = 16807
genBFactor = 48271

genAdivisior = 4
genBdivisior = 8

division = 2147483647

matches = 0

bitwise16 = int("1111111111111111",2)

numIterations = 5000000
i = 0

while i < numIterations:
    genA = (genA * genAFactor) % division
    while (genA % genAdivisior != 0):
        genA = (genA * genAFactor) % division

    genB = (genB * genBFactor) % division
    while (genB % genBdivisior != 0):
        genB = (genB * genBFactor) % division

    genAbin = genA & bitwise16
    genBbin = genB & bitwise16

    if genAbin == genBbin:
        matches += 1

    i += 1

print(matches)
