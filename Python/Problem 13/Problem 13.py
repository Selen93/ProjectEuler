# First 10 digits of the sum of the 50 numbers in the numbers file

f = open('numbers')
numbers = []
number = 0
sum = 0
sums = []
sumofsums = 0
i = 0

for x in f:
    numbers.append(int(x))
    i+=1

i = 0
for m in range(0,50):
    for n in range(0,100):
        number = numbers[n]
        number = str(number)
        number = number[m:m+1]
        sum += int(number)
    sums.append(sum)
    sum = 0
print(sums)

for sum in sums:
    sums[i]*=10**-i
    i+=1
print(sums)

for sum in sums:
    sumofsums+=sum
print(sumofsums)