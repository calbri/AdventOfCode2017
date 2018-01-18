f = open("13input.txt")

layers = {}
scanners = {}

layersWithScanners = []

for layer in f.readlines():
    layerVal = int(layer.split(": ")[0])
    depth = int(layer.split(": ")[1].rstrip())

    layers[layerVal] = depth + depth - 2
    layersWithScanners.append(layerVal)

maxVal = layerVal

foundSolution = False
delay = 0

while foundSolution == False:
    packetPosition = 0
    caught = False
    numTicks = 0

    while packetPosition <= maxVal:
        if packetPosition in layersWithScanners:
            if ((packetPosition + delay) % layers[packetPosition]) == 0:
                caught = True
                break

        packetPosition += 1

    if not(caught):
        foundSolution = True
    else:
        delay += 1

print(delay)
