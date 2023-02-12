# Exercise 2: Good Morning Sir

# Create a python program capable of greeting you with good morning. GA and GE. your program should use timestamp module to get the current hour.
# time module is used along with strftime function, which returns the current time of the device.

import time
timestamp = int(time.strftime("%H"))   #the function returns the ans in str format, we need to convert it in int.
if (timestamp>0 and timestamp<25):
    if(timestamp>4 and timestamp<12):
        print("Good Morning Sir")
    elif(timestamp>=12 and timestamp<(12+5)):
        print("Good Afternoon Sir")
    elif(timestamp>=(12+5) or timestamp<=4):
        print("Good Night Sir")
else:
    print("The Time is incorrect")


 