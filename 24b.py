import copy

f = open("24input.txt")

bridges = {}

i = 0
for bridge in f.readlines():
    start = int(bridge.rstrip().split("/")[0])
    end = int(bridge.rstrip().split("/")[1])

    bridges[i] = [start, end]

    i += 1

paths = set([])

for key in bridges:
    if bridges[key][0] == 0:
        paths.add((frozenset([key]), bridges[key][1]))
    if bridges[key][1] == 0:
        paths.add((frozenset([key]), bridges[key][0]))

while True:
    newAddition = False
    for path in paths.copy():
        for key in bridges:
            if bridges[key][0] == path[1]:
                if key in path[0]:
                    continue
                newPath = (frozenset(path[0].union(frozenset([key]))), bridges[key][1])
                if not(newPath in paths):
                    paths.add(newPath)
                    newAddition = True
            elif bridges[key][1] == path[1]:
                if key in path[0]:
                    continue
                newPath = (frozenset(path[0].union(frozenset([key]))), bridges[key][0])
                if not(newPath in paths):
                    paths.add(newPath)
                    newAddition = True
    if not(newAddition):
        break

highestStrength = 0
maxLength = 0

for path in paths:
    currentStrength = 0
    for bridge in path[0]:
        currentStrength += bridges[bridge][0]
        currentStrength += bridges[bridge][1]
    if currentStrength > highestStrength:
        if len(path[0]) >= maxLength:
            highestStrength = currentStrength
            maxLength = len(path[0])
    elif len(path[0]) > maxLength:
        highestStrength = currentStrength
        maxLength = len(path[0])

print(highestStrength)
