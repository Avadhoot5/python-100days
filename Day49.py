# File IO FILE HANDLING

# before we can perform any operations on a file, we must open it 

# Reading a file, r is the default method.
# if file is not present , error is thrown 

with open('opening.txt', 'r') as f:
    o = f.read()
    print(o)

# Writing into a file, if file is not present it gets created and write methods writes the content passed to it.
# contents are replaced each time we write into the file 

with open('opening2.txt', 'w') as f2:
    f2.write('This is written using file handling method')

# Append method, used to add contents at the end of the file.

with open('opening2.txt', 'a') as f2:
    f2.write('this string is appended')

# Creating a file using create method(x)
# with open('opening3.txt', 'x') as f3:
#     pass

# Text (t) 'rt' == 'r', here t mode is used to handle text files, as t is default we don't use rt.

# Binary(b), used to handle binary files. (eg. images, pdfs, etc)

# rb, reading as binary
# with open('dinos.png', 'rb') as img:
#     print(img.read())