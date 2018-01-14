f = open("11input.txt")

directions = f.readlines()[0].rstrip().split(",")

reverses = [["n", "s"], ["sw", "ne"], ["nw", "se"]]
simplifications = [["ne", "nw", "n"], ["se", "sw", "s"], ["sw", "n", "nw"],
                   ["nw", "s", "sw"], ["ne", "s", "se"], ["se", "n", "ne"]]

solutions = []
currentMaxDistance = 0

# reverse all directions
for direction in directions:
    for reverse in reverses:
        if direction == reverse[0]:
            solutions.append(reverse[1])
        elif direction == reverse[1]:
            solutions.append(reverse[0])

    while True:
        changesMade = False

        # check for cancellations
        for reverse in reverses:
            if (reverse[0] in solutions) and (reverse[1] in solutions):
                solutions.remove(reverse[0])
                solutions.remove(reverse[1])
                changesMade = True

        # check for simplifications
        for simplification in simplifications:
            if (simplification[0] in solutions) and (simplification[1] in solutions):
                solutions.append(simplification[2])
                solutions.remove(simplification[1])
                solutions.remove(simplification[0])
                changesMade = True

        if not(changesMade):
            break

    if currentMaxDistance < len(solutions):
        currentMaxDistance = len(solutions)

print(currentMaxDistance)
