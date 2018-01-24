import numpy as np
f = open("21input.txt")

art = np.array([[0, 1, 0],[0, 0, 1],[1, 1, 1]])
size = 3

rules = []

for line in f.readlines():
    rule = []

    startConfig = line.rstrip().split(" => ")[0]
    endConfig = line.rstrip().split(" => ")[1]

    startRule = []
    for startLine in startConfig.split("/"):
        ruleLine = []
        for c in startLine:
            if c == ".":
                ruleLine.append(0)
            else:
                ruleLine.append(1)
        startRule.append(ruleLine)

    endRule = []
    for endLine in endConfig.split("/"):
        ruleLine = []
        for c in endLine:
            if c == ".":
                ruleLine.append(0)
            else:
                ruleLine.append(1)
        endRule.append(ruleLine)

    rules.append([np.asarray(startRule), np.asarray(endRule)])

numIterations = 5

for i in range(0, numIterations):
    divisor = 0
    if (size % 2 == 0):
        divisor = 2
    else:
        divisor = 3

    ruleCombinations = [[0 for x in range(size // divisor)] for y in range(size // divisor)]
    for j in range(0, size // divisor):
            for k in range(0, size // divisor):
                element = np.copy(art[divisor*j:(divisor*j)+divisor, divisor*k:(divisor*k)+divisor])
                foundMatch = False
                for i in range(0,5):
                    for rule in rules:
                        if (element.size != rule[0].size):
                            continue
                        if(np.array_equal(element,rule[0])):
                            foundMatch = True
                            ruleCombinations[j][k] = rule[1]
                            break
                    element = np.rot90(element)

                if not(foundMatch):
                    element = np.flipud(element)
                    for rule in rules:
                        if (element.size != rule[0].size):
                            continue
                        if(np.array_equal(element,rule[0])):
                            foundMatch = True
                            ruleCombinations[j][k] = rule[1]
                if not(foundMatch):
                    element = np.flipud(element)
                    element = np.fliplr(element)
                    for rule in rules:
                        if (element.size != rule[0].size):
                            continue
                        if(np.array_equal(element,rule[0])):
                            foundMatch = True
                            ruleCombinations[j][k] = rule[1]

                if not(foundMatch):
                    print("Error!")
    newArt = ruleCombinations[0][0]
    for k in range(1, size // divisor):
        newArt = np.concatenate((newArt,ruleCombinations[0][k]), axis=1)
    for j in range(1, size // divisor):
        toAppend = ruleCombinations[j][0]
        for k in range(1, size // divisor):
            toAppend = np.concatenate((toAppend,ruleCombinations[j][k]), axis=1)
        newArt = np.concatenate((newArt,toAppend), axis=0)

    art = newArt
    size = art.shape[0]

numPixels = 0
for i in range(0, size):
    for j in range(0, size):
        if art[i][j] == 1:
            numPixels += 1

print(numPixels)
