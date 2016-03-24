# smallest positive number which is evenly divisible by all numbers from 1 to 20
import math

def lcm(n,m):
    if n>m:
        greater=n
    else:
        greater=m
    while True:
        if greater%n==0 and greater%m==0:
            lcm = greater
            break
        greater+=1

    return lcm

result = 1
for i in range(1,20):
    result = lcm(result,i)

print(result)




