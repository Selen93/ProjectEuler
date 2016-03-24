# Largest prime factor of 600851475143
import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

number = 600851475143
upperbound = math.sqrt(number)

for x in range(2,int(upperbound)):
    if isPrime(x):
        if number%x == 0:
            print(x)