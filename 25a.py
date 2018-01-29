f = open("25input.txt")

state = f.readline().rstrip().split("state ")[1].split(".")[0]
checksum = int(f.readline().rstrip().split("after ")[1].split(" steps")[0])

states = {}
stateToRead = ""
currentVal = 0

for line in f.readlines():
    if "In state" in line:
        stateToRead = line.rstrip().split("state ")[1].split(":")[0]
        states[stateToRead] = [[],[]]

    if "If the current value" in line:
        currentVal = int(line.rstrip().split("is ")[1].split(":")[0])

    if "Write the value" in line:
        states[stateToRead][currentVal].append(int(line.rstrip().split("value ")[1].split(".")[0]))

    if "Move one slot" in line:
        if line.rstrip().split("to the ")[1].split(".")[0] == "left":
            states[stateToRead][currentVal].append(-1)
        else:
            states[stateToRead][currentVal].append(1)

    if "Continue with" in line:
        states[stateToRead][currentVal].append(line.rstrip().split("state ")[1].split(".")[0])

position = 0
locationsWith1 = set([])


for i in range(0, checksum):
    #value to write
    value = 0
    if position in locationsWith1:
        value = 1

    if states[state][value][0] == 1:
        locationsWith1.add(position)
    else:
        locationsWith1.discard(position)

    #direction to move
    position += states[state][value][1]

    #new state
    state = states[state][value][2]

print(len(locationsWith1))
