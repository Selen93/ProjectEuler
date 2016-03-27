# Number letter counts from 1 to 1000
import time

start_time = time.clock()
numbers = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:10,1000:11}
count = 0

#numbers from 21 to 99
for n in range(20,91,10):
    for i in range(1,10):
        numbers[i+n] = numbers.get(n) + numbers.get(i)

#numbers 200,300,400...
for i in range(200,1000,100):
    numbers[i] = numbers[i/100]+7

#numbers 101...199,201...299,...
for i in range(100,1000,100):
    for n in range(1,100):
            numbers[i+n] = numbers[i]+numbers[n]+3

for key in numbers:
    count += numbers.get(key)

print(count)
print("--- %s seconds ---" % (time.clock() - start_time))
