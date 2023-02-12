# seek(), tell() and other functions 

# seek() and tell() func. are used to work with file objects & their positions within a file 

# seek() - allows you to move current position within a file to a specific point. Position is defined in bytes, you can move forward/backward from the current position.
# tell() - returns the current position within the files, in bytes.

with open('seeking.txt', 'w') as f:
    f.write('Hello World')

with open('seeking.txt', 'r') as f:
    f.seek(4) # moves to the 4th byte in the file
    prev_pos = f.tell()
    pr = f.read(5) # reads the next 5 bytes
    print(pr)
    current_pos = f.tell()
    print("the earlier positon was", prev_pos)
    print("the current position is ", current_pos)

# truncte() is used to truncate  the file to a specific size

with open('truncating.txt', 'w') as f:
    f.write('this is an example for truncate function')
    f.truncate(10) # open the truncating file to see the execution


