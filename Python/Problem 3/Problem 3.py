# Largest prime factor of 600851475143
import math

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

zahl = 600851475143
grenze = math.sqrt(zahl)

for x in range(2,int(grenze)):
    if isPrime(x):
        if zahl%x == 0:
            print(x)