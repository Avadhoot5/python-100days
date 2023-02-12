# Exercise 4: Secret Code Language

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random, string

# taking user input to ask for coding or decoding the message

status = int(input("Do you want to code or decode the message, 0 - Code, 1 - Decode: "))
try:
    if(status == 0 or status == 1):
        pass
    else:
        print("Please provide a valid response")
except ValueError:
    print("Please provide your response as 0 or 1")

# CODING THE STRING

#choosing random 3 letters from the string

seq = string.ascii_lowercase

# Reversing the string if characteres less than 3

def rev(singlechar):
    print(singlechar[::-1], end = " ")

# Length greater than 3, coding the string

def ran(singlechar):
    txt = singlechar
    firstl = singlechar[0]
    right = txt.lstrip(firstl)
    # joining = rc_1 + rc_2 + rc_3 + right + firstl + rc_1 + rc_2 + rc_3
    joining = random.choice(seq) + random.choice(seq) + random.choice(seq) + right + firstl + random.choice(seq) + random.choice(seq) + random.choice(seq)
    print(joining, end = " ")

# Iterating over each character 

# Taking user input for coding

if(status == 0):
    word = input("enter your message to code: ")
    new = word.split(" ")
    for singlechar in new:
        # print(singlechar)
        if(len(singlechar) < 3):
            rev(singlechar)
        else:
            ran(singlechar)

# DECODING THE STRING

def rev_s(sc):
    print(sc[::-1], end = " ")

def ran_s(sc):
    txt = sc[3:-3]
    last_char = txt[-1]
    txt_2 = txt.rstrip(last_char)
    original = last_char + txt_2
    print(original, end = " ")


# Taking user input for decoding
if(status == 1):
    word_1 = input("enter your message to decode: ")
    new_1 = word_1.split(" ")
    for sc in new_1:
        if(len(sc) < 3):
            rev_s(sc)
        else:
            ran_s(sc)



    



