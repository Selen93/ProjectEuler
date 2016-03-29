# DESC: Evaluate the sum of all the amicable numbers under 10000.
import time
import help

start_time = time.clock()
sum = 0

for i in range(1,10000):
    div = help.divisorsum(i)
    if help.divisorsum(div)==i:
        if div != i: sum+=i

print(sum)
print("--- %s seconds ---" % (time.clock() - start_time))

