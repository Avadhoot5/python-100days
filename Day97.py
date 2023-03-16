# Multithreading 

import threading, time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

# Normal Code 
# time1 = time.perf_counter()
# func(4)
# func(2)
# func(3)
# time2 = time.perf_counter()
# print(time2 - time1)

# Same code using Threads
def main():
    t1 = threading.Thread(target = func, args=[4])
    t2 = threading.Thread(target = func, args=[2])
    t3 = threading.Thread(target = func, args=[3])

    time3 = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()

    t1.join() # wait until t1 is completed
    t2.join() # wait until t2 is completed
    t3.join() # wait until t3 is completed
    time4 = time.perf_counter()
    print(time4 - time3)

# using ThreadPoolExecutor for executing multiple tasks
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 4)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 1)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3, 5, 1 , 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()
