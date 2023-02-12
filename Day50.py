# read(), readlines() and other methods 

# readline() - method. reads one line at a time

# with open('reading.txt','r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)
    
# readlines() method - reads all the lines of the file & returns them as a list of strings.

with open('reading.txt','r') as f:
    line = f.readlines()
    # print(line)
    for i in line:
        print(i)

# writelines() method - writes a sequence of strings to a file. the seq. can be list/tuple

# creating a file and appending lines 

# with open('reading.txt', 'a') as f:
#      li = ['This is line 1','This is line 2','This is line 3','This is line 4']
#      for i in li:
#           f.write(i + '\n')