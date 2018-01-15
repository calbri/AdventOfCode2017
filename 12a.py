f = open("12input.txt")
programs = {}

for prog in f.readlines():
    num = int(prog.split(" ")[0])

    connections = []

    for con in prog.split("<-> ")[1].split(", "):
        connections.append(int(con.rstrip()))

    programs[num] = connections

checked = []
unchecked = [0]

while len(unchecked) != 0:
    num = unchecked.pop()
    checked.append(num)

    for con in programs[num]:
        if not(con in checked) and not(con in unchecked):
            unchecked.append(con)

print(len(checked))


        
