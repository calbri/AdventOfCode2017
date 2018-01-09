numString = input()
firstDigit = numString[0]
stringLength = len(numString)

matchSum = 0
i = 0
for c in numString:
    if (i != stringLength - 1):
        if (c == numString[i+1]):
            matchSum += int(c)
    else:
        if (c == firstDigit):
            matchSum += int(c)
    i += 1

print(matchSum)    
