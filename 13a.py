f = open("13input.txt")

layers = {}
scanners = {}

layersWithScanners = []

for layer in f.readlines():
    layerVal = int(layer.split(": ")[0])
    depth = int(layer.split(": ")[1].rstrip())

    layers[layerVal] = depth
    scanners[layerVal] = [0, True]

    layersWithScanners.append(layerVal)

maxVal = layerVal

packetPosition = 0
severity = 0

while packetPosition <= maxVal:

    #check for collision
    if packetPosition in layersWithScanners:
        if scanners[packetPosition][0] == 0:
            severity += layers[packetPosition] * packetPosition

    #move one over
    packetPosition += 1

    #update scanners
    for layer in scanners:
        if scanners[layer][1]:
            if scanners[layer][0] == layers[layer] - 1:
                scanners[layer][1] = False
                scanners[layer][0] -= 1
            else:
                scanners[layer][0] += 1
        else:
            if scanners[layer][0] == 0:
                scanners[layer][1] = True
                scanners[layer][0] += 1
            else:
                scanners[layer][0] -= 1

print(severity)
