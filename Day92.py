# Function Caching 

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(20))
print("20 done")
print(fx(2))
print("2 done")
print(fx(15))
print("15 done")

# used lru cache, below inputs are being repeated, it gets executed faster
print(fx(20))
print("20 done")
print(fx(2))
print("2 done")
print(fx(15))
print("15 done")

#new input passed
print(fx(12))
print("12 done")

