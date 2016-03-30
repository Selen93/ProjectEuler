# DESC: What is the total of all the name scores in the file?
#       Name score: rank times sum of characters value
#       A = 1 B = 2 ...
import string
import time
import help

file = open("p022_names.txt")
names = []
total = 0
start_time = time.clock()

row = file.readline()
names = sorted([x[1:len(x)-1] for x in row.split(',')])

for i in range(len(names)):
    total += help.alpval(names[i])*(i+1)

print(total)
print("--- %s seconds ---" % (time.clock() - start_time))