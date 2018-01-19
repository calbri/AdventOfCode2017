positions = {}
numPrograms = 16

i = 0
for p in range(ord('a'), ord('p') + 1):
    positions[chr(p)] = i
    i += 1

f = open("16input.txt")

for move in f.readlines()[0].split(","):
    if move[0] == "s":
        numMoves = int(move.rstrip()[1:])

        for p in positions:
                positions[p] = (positions[p] + numMoves) % 16

    elif move[0] == "x":
        exchange = move.rstrip()[1:]
        first = int(exchange.split("/")[0])
        second = int(exchange.split("/")[1])

        firstProg = ""
        secondProg = ""

        for p in positions:
            if positions[p] == first:
                firstProg = p
            if positions[p] == second:
                secondProg = p

        positions[firstProg] = second
        positions[secondProg] = first

    elif move[0] == "p":
        exchange = move.rstrip()[1:]
        firstProg = exchange.split("/")[0]
        secondProg = exchange.split("/")[1]

        firstPos = positions[firstProg]
        secondPos = positions[secondProg]

        positions[firstProg] = secondPos
        positions[secondProg] = firstPos

end = ["-" for x in range(0, numPrograms)]

for p in positions:
    end[positions[p]] = p

endString = ""

for p in end:
    endString += p

print(endString)
