def findDivision(numString):
    for num1 in numString.split("\t"):
        for num2 in numString.split("\t"):
            intNum1 = int(num1)
            intNum2 = int(num2)

            if intNum1 > intNum2:
                if (intNum1 % intNum2 == 0):
                    return intNum1 / intNum2

import math
f = open("2input.txt")

checksum = 0

for numString in f.readlines():
    checksum += findDivision(numString)

print(checksum)
