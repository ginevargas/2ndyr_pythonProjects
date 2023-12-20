import time

#A sample function whose time taken to be measured
def fun():
    #insert some code here to test runtime
    prod = 3
    n = 100  # value to be changed
    i = 1
    while i <= n:
        for j in range(0, n):
            prod = prod * n
            print(" prod ", end='')
        print(prod, end='\n')
        i = i * 2





# get the start time
st = time.time()

# main program
fun()

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')