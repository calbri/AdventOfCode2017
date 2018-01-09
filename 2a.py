import math
f = open("2input.txt")

checksum = 0

for numString in f.readlines():
    small = math.inf
    big = 0

    for num in numString.split("\t"):
        if int(num) < small:
            small = int(num)
        if int(num) > big:
            big = int(num)

    checksum += big - small

print(checksum)
