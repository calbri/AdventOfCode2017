f = open("4input.txt")

validCount = 0

for passPhrase in f.readlines():
    words = []
    validPassPhrase = True
    for word in passPhrase.split():
        if word in words:
            validPassPhrase = False
            break
        else:
            words.append(word)
    if validPassPhrase:
        validCount += 1

print(validCount)
