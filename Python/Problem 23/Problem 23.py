# DESC: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import help
import time

start_time = time.clock()
abundant = []
numbers = []

for i in range(1,20162):
    if help.divisorsum(i) > i: abundant.append(i)

for i in range(len(abundant)):
    for n in range(len(abundant)):
        number = abundant[i]+abundant[n]
        if number < 20162: numbers.append(number)

print(sum(set(range(20162))-set(numbers)))
print("--- %s seconds ---" % (time.clock() - start_time))