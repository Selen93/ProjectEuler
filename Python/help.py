# help functions

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

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

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

def triangular(n):
    result = 0
    for i in range (1,n+1):
        result+=i
    return result
