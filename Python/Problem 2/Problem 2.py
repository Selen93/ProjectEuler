# Sum of even Fibonacci Numbers until 4 Million


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


result = 0
fibonaccinumbers = list()
x=0

while True:
    x = x+1
    if F(x) >= 4000000:
        break
    fibonaccinumbers.append(F(x))

for x in fibonaccinumbers:
    if x%2==0:
        result = result +x

print(result)