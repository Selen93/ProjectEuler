# Longest Collatz Sequence under 1 million
import help
import time

result = 0
length = 0
lengths = dict()
start_time = time.time()

for n in range (1,1000001):
    if n/2 in lengths: lengths.update({n:lengths[n/2]+1})
    else: lengths.update({n:help.collatzlength(n)})
    if length < lengths[n]:
        length = lengths[n]
        result = n

print(result)
print("--- %s seconds ---" % (time.time() - start_time))
