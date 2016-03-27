# DESC: Find the maximum total from top to bottom of the triangle in triangle.txt
# WOULDBENICE: Each list in maximums has one extra 0 at the end. I can't figure out why it needs to be that way.
import time
import help
import math

start_time = time.clock()
file = open('triangle')
numbers = [] # each row of triangle.txt will be saved here
maximums = [] # each maximum of the two numbers  leading to a number plus the number itself will be saved here.

for row in file:
    numbers.append(str(row).replace(" ","").replace("\n","")) # strings are easier because all numbers will have 2 digits anyway
    maximums.append([0]*(int(math.ceil(len(row)/3))+1)) # initialize empty lists of maximums. each list has one more item than the last

maximums[0][0]=75 # first maximum set to the first number, because it does not have any number leading to it.

for i in range(1,len(numbers)): #going over each row of numbers in the triangle
    for n in range(0,len(numbers[i]),2): # because the numbers are stored in string format, you need to have a step value of 2.
        if(n/2)>0:
            maximums[i][int(n/2)] = max((maximums[i-1][int(n/2)]+help.mk_int(numbers[i][n:n+2])),(maximums[i-1][int(n/2)-1])+help.mk_int(numbers[i][n:n+2]))
            # the new maximum of a number is the maximum of the value of the number itself + the left maximum leading to it
            # and the value of the number itself + the right maximum leading to it.

print(max(maximums[14])) #print the result
print("--- %s seconds ---" % (time.clock() - start_time)) #yay 0.5 milliseconds

