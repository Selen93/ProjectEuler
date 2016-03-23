# Sum of Divisibles of 3 and 5 until 1000

result = 0

for x in range(1,1000):
    if x%3==0 or x%5==0:
        result = result + x

print(result)