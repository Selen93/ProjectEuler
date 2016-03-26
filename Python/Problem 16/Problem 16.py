# Sum of digits of 2^1000

number = str(2**1000)
result = 0

for i in range(302):
    result += int(number[i:i+1])

print(result)