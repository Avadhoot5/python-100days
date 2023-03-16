# Time Module 

import time

def usingWhile():
    i = 0
    while i<1000:
        i = i + 1
        print(i)

def usingFor():
    for i in range(1000):
        print(i)

# time.time() - returns the current time as a floating point no, representing the no of seconds since the epoch

# init = time.time()
# usingFor()
# t1 = time.time() - init

# init = time.time()
# usingWhile()
# t2 = time.time() - init

# print(t1)
# print(t2)

print(time.time())

# time.sleep() - halts the execution of the current thread for specified no of seconds.

print('Test message, next message will be printed after 4 seconds')
# time.sleep(4)
print("Message is printed")

t = time.localtime()
# print(t)
formatted_time = time.strftime("%Y %m %d, %H:%M:%S", t)
print(formatted_time)

