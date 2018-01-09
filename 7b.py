def getWeight(prog, programs):
    if prog.children == []:
        return prog.weight
    else:
        total = 0
        for child in prog.children:
            total += getWeight(getProgramByName(child, programs), programs)
        total += prog.weight
        return total

def getProgramByName(progName, programs):
    for prog in programs:
        if prog.name == progName:
            return prog


def areAbovePathsBalanced(prog, programs):
    weights = []
    for child in prog.children:
        weights.append(getWeight(getProgramByName(child, programs), programs))

    occurrences = {}
    occurred = []

    for weight in weights:
        if weight in occurred:
            occurrences[weight] += 1
        else:
            occurrences[weight] = 1
        occurred.append(weight)

    print(occurrences)

    indexToCheck = -1
    goalWeight = 0
    for weight in occurrences:
        if occurrences[weight] == 1:
            for num, pathWeight in enumerate(weights):
                if weight == pathWeight:
                    indexToCheck = num
        else:
            goalWeight = weight

    if indexToCheck == -1:
        return True
    else:
        return False

def getOddOneOut(paths, programs):
    weights = []
    for child in paths:
        weights.append(getWeight(getProgramByName(child, programs), programs))

    print(weights)

    occurrences = {}
    occurred = []

    for weight in weights:
        if weight in occurred:
            occurrences[weight] += 1
        else:
            occurrences[weight] = 1
        occurred.append(weight)

    print(occurrences)

    indexToCheck = -1
    goalWeight = 0
    for weight in occurrences:
        if occurrences[weight] == 1:
            for num, pathWeight in enumerate(weights):
                if weight == pathWeight:
                    indexToCheck = num
        else:
            goalWeight = weight

    if indexToCheck == -1:
        for child in paths:
            return getOddOneOut(getProgramByName(child, programs).children, programs)
    else:
        print("one weight is different, checking that odd one")
        if (areAbovePathsBalanced(getProgramByName(paths[indexToCheck], programs), programs)):
            print("problem is the current level, weight needs to be: ")
            return getProgramByName(paths[indexToCheck], programs).weight + (goalWeight - weights[indexToCheck])

        else:
            print("problem exists higher up")
            return getOddOneOut(getProgramByName(paths[indexToCheck], programs).children, programs)





class Program:

    def __init__(self, name, children, weight):
        self.name = name
        self.children = children
        self.weight = weight

programs = []

f = open("7input.txt")

for prog in f.readlines():
    name = prog.split(" ")[0]
    weight = int(prog.split(" ")[1].split(" ")[0].rstrip().strip(')').strip('('))

    childPrograms = []

    if "->" in prog:
        childPrograms = prog.split(" -> ")[1].split(", ")
        for num, child in enumerate(childPrograms):
            childPrograms[num] = child.rstrip()

    newProgram = Program(name, childPrograms, weight)

    programs.append(newProgram)

progHasParent = {}
rootProgram = None

for prog in programs:
    progHasParent[prog.name] = False

for prog in programs:
    for progName in prog.children:
        progHasParent[progName] = True

for key in progHasParent:
    if not(progHasParent[key]):
        for prog in programs:
            if prog.name == key:
                rootProgram = prog
                break

paths = rootProgram.children

print(getOddOneOut(paths, programs))
