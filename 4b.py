f = open("4input.txt")

validCount = 0

for passPhrase in f.readlines():
    validPassPhrase = True
    index1 = 0
    for word1 in passPhrase.split():
        index2 = 0
        sortedFirstWord = ''.join(sorted(word1))
        if not(validPassPhrase):
            break
        for word2 in passPhrase.split():
            if index1 == index2:
                continue
            if sortedFirstWord == ''.join(sorted(word2)):
                validPassPhrase = False
                break
            index2 += 1
        index1 += 1
    if validPassPhrase:
        validCount += 1

print(validCount)
