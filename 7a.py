class Program:

    def __init__(self, name, children):
        self.name = name
        self.children = children

programs = []

f = open("7input.txt")

for prog in f.readlines():
    name = prog.split(" ")[0]
    childPrograms = []

    if "->" in prog:
        childPrograms = prog.split(" -> ")[1].split(", ")
        for num, child in enumerate(childPrograms):
            childPrograms[num] = child.rstrip()

    newProgram = Program(name, childPrograms)

    programs.append(newProgram)

progHasParent = {}

for prog in programs:
    progHasParent[prog.name] = False

for prog in programs:
    for progName in prog.children:
        progHasParent[progName] = True

for key in progHasParent:
    if not(progHasParent[key]):
        print(key)
        break
