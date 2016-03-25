# first triangular number with over 500 divisors
import help

i = 1
triangular = 0
divisors = 0

while True:
    triangular = help.triangular(i)
    for n in range(2,int(triangular**0.5)+1):
        if triangular%n == 0:
            divisors+=1
    divisors*=2
    print("triangular = "+str(triangular))
    print("divisors: "+str(divisors))
    if divisors > 500:
        print(triangular)
        break
    else:
        divisors = 0
    i+=1
