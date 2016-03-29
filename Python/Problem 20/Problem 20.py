# DESC: Find the sum of the digits in the number 100!
import math
import time

start_time = time.clock()

print(sum(map(int, (list(str(math.factorial(100)))))))
print("--- %s seconds ---" % (time.clock() - start_time))
