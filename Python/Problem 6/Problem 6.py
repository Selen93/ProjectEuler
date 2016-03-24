# Difference of Square Sum and Sum of Squares of first 100 natural numbers

result1 = 0
result2 = 0

for i in range (1,101):
    result1+=i**2
    result2+=i

result2 = result2**2
print (abs(result2-result1))