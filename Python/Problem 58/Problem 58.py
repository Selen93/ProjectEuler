# Square Spirals
import math
import time
import help

number = 1
primes = set()
diagonalnumbers = set()
ratio = 0.00
sidelength = 3
eins = True
start_time = time.time()

while True:
    squarenumber = sidelength**2
    for m in range(number,squarenumber+1,sidelength-1):
        if help.isPrime(m): primes.add(m)
        diagonalnumbers.add(m)
    number = sidelength**2
    if eins:
        diagonalnumbers.remove(1)
        eins = False
    ratio = (len(primes.intersection(diagonalnumbers)))/len(diagonalnumbers)
    if ratio <= 0.10:
        print(sidelength)
        print("--- %s seconds ---" % (time.time() - start_time))
        break
    sidelength+=2




