# DESC: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import help
import time

i = 3
fibo = {"1":1,"2":1}
start_time = time.clock()

while True:
    fibo[str(i)] = fibo[str(i-2)]+fibo[str(i-1)]
    if len(str(fibo[str(i)])) == 1000:
        print(i)
        break
    i+=1
print("--- %s seconds ---" % (time.clock() - start_time))