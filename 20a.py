class Particle:

    def __init__(self, position, velocity, acceleration, counter):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.index = counter

    def getDistance(self):
        sum = 0
        for p in self.position:
            sum += abs(p)

        return sum

    def updateVelocity(self):
        for i in range(0, len(self.acceleration)):
            self.velocity[i] += self.acceleration[i]

    def updatePosition(self):
        for i in range(0, len(self.velocity)):
            self.position[i] += self.velocity[i]

    def update(self):
        self.updateVelocity()
        self.updatePosition()

f = open("20input.txt")

particles = []

counter = 0
for p in f.readlines():
    positions = p.split(">, ")[0].split("p=<")[1].split(",")

    posVector = []
    for pos in positions:
        posVector.append(int(pos))

    velocities = p.split(">, ")[1].split("v=<")[1].split(",")

    velVector = []
    for vel in velocities:
        velVector.append(int(vel))

    accelerations = p.rstrip().split(">")[2].split("a=<")[1].split(",")

    accVector = []
    for acc in accelerations:
        accVector.append(int(acc))

    particle = Particle(posVector, velVector, accVector, counter)

    particles.append(particle)

    counter += 1

numIterations = 1000

for i in range(0, numIterations):
    for p in particles:
        p.update()

print(min(particles, key=lambda p: p.getDistance()).index)
