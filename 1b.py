numString = input()
firstDigit = numString[0]
stringLength = len(numString)
offset = int(stringLength / 2)

matchSum = 0
i = 0
for c in numString:
    if (i < stringLength - offset):
        if (c == numString[i+offset]):
            matchSum += int(c)
    else:
        if (c == numString[offset - (stringLength - i)]):
            matchSum += int(c)
    i += 1

print(matchSum)
