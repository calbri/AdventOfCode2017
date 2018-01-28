#In order for the loop to terminate,
#  g = b - c = 0 must be True
#Therefore, the loop runs 1000 times, as c = b + 17000, and b is incremented
#by 17 each time.

#h is incremented by 1 when f is equal to 0

#f is equal to 0 when g = d*e - b = 0

#d starts at 2 and is incremented by 1 every big loop
#e starts at 2 and is incremented by 1 each small loop

#The big loop occurs from d = 0 to b
#The small loop occurs from e = 0 to b

#Since the loops cover all numbers from 1 to b, if there exists two numbers
#between 2 and b that multiply to give b, then h is incremented

#In other words, if b is non-prime then h gets incremented.

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i == 0):
                return False
        return True
    else:
        return False
b = 81
c = b

b *= 100
b += 100000

c = b
c += 17000

numHincrements = 0

while (True):
    if not(isPrime(b)):
        numHincrements += 1

    if (b - c == 0):
        break
    else:
        b += 17

print(numHincrements)
