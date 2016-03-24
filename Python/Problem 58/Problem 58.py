# Square Spirals
import math
import time

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

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
        if isPrime(m): primes.add(m)
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




