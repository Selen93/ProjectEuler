# What is the 10001st Prime?
import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

n = 0
i = 2

while True:
    if isPrime(i): n+=1
    if n == 10001:
        print (i)
        break
    i+=1
