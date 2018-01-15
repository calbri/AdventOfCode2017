f = open("12input.txt")
programs = {}

for prog in f.readlines():
    num = int(prog.split(" ")[0])

    connections = []

    for con in prog.split("<-> ")[1].split(", "):
        connections.append(int(con.rstrip()))

    programs[num] = connections

numRounds = 0
checked = []
unchecked = []

for i in range(0, len(programs)):
    if not(i in checked):
        unchecked.append(i)
    else:
        continue

    while len(unchecked) != 0:
        num = unchecked.pop()
        checked.append(num)

        for con in programs[num]:
            if not(con in checked) and not(con in unchecked):
                unchecked.append(con)

    numRounds += 1

print(numRounds)
