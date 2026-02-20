# List, reversing the list, poping the last element and placing it in the first element of the another list, and compare the first and last list
# this is a DSA topic

# l1 = [25,16,14,34]
# l2 = l1.copy()
# l2.reverse()
# print(l2)
# # print(l2)

# l3 = []

# for i in l2:
#     l3.insert(0,i)

# print(l3)

# fruits = ['apple', 'banana', 'cherry']
# new = []
# for i in fruits:
# 	new.insert(0,i)

# print(new)

# n = int(input("Enter a no to find its sum:"))
# def sumof(n):
# 	sum = 0
# 	for i in range(n):
# 		sum = sum + i
# 	return sum

# print(sumof(3))

# n = int(input("Enter a no to find its sum:"))
# sum = 0
# for i in range(1,n+1):
# 	sum = sum + i
# print(sum)


# if(not os.path.exists("data")):
#     os.mkdir("data")

# a = os.listdir("data")
# print(a)

# # mkdir - makes a directory, replace/rename - changes the name of the directory

# for i in range(0,100):
#     # os.mkdir(f"data/Day{i+1}")
#     os.replace(f"data/Day{i+1}", f"data/Day{i+1}")

# Reversing List and comparing it with another list 
# n = int(input("enter the size of the list: "))
# size = n
# l1 = []
# l2 = []

# i = 0
# while i < size:
#     a = int(input(""))
#     l1.append(a)
#     i = i + 1

# # print(l1)
# # # l1.reverse()
# # for i in l1:
# #     l2.insert(0, i)

# # newl1 = l1.copy()
# # print(newl1)
# # newl1.reverse()
# # print(newl1)
# # print(l2)

# # for i in l1:
# #     a = l1.pop()
# #     l2.append(a)

# # print(l1)
# # print(l2)
# # newl1 = l1

# if newl1 == l2:
#     print("List is reversed")
# else:
#     print("List is NOT reversed")




# if user writes quit , no error should be displayed,
# but if user writes another string the error should be displayed

# Rasing error if string is not quit

# a = input('write something: ')
# if (a != 'quit'):
#     raise ValueError('enter properly')



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

# import random, string

# seq = string.ascii_lowercase
# randomChar = random.choice(seq)

# status = int(input('Do you want to code or decode the message, 0 - Code, 1 - Decode: '))
# try:
#     if (status == 0 or status == 1):
#         pass
#     else:
#         print('Please provide a valid response')
# except ValueError as v:
#     print('Please enter integer value 0 or 1')

# # decoding the message

# def revS(value):
#     return value[::-1]

# def encodeMessage(text):
#     firstChar = text[0]
#     text = text[1:] + firstChar
#     text = random.choice(seq) + random.choice(seq) + random.choice(seq) + text + random.choice(seq) + random.choice(seq) + random.choice(seq)
#     return text

# if (status == 0):
#     userMessage = input('Enter your message to code: ')
#     codedMessage = ''
#     for eachChar in userMessage.split(' '):
#         if (len(eachChar) < 3):
#             codedMessage += revS(eachChar) + ' '
#         else:
#             codedMessage += encodeMessage(eachChar) + ' '
#     print(codedMessage)

# # encoding the message

# def decodeMessage(text):
#     trimText = text[3:-3]
#     swapText = trimText[-1] + trimText[:-1]
#     return swapText

# if (status == 1):
#     userMessage = input('Enter your message to Decode: ')
#     originalMessage = ''
#     for eachChar in userMessage.split(' '):
#         if (len(eachChar) < 3):
#             originalMessage += revS(eachChar) + ' '
#         else:
#             originalMessage += decodeMessage(eachChar) + ' '
#     print(originalMessage)


# from PIL import Image

# imageURL = 'C:\\Users\\username\\Pictures\\Screenshots\\Fact.png'

# def imageView(path):
#     im = Image.open(f'{path}')
#     im.show()

# imageView(imageURL)


# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def showInfo(self):
#         print(f'Employee {self.name} is of age {self.age}')
# class Manager(Employee):

#     def task(self):
#         print('The manager is managing employees')
    

# emp1 = Employee('rakesh', 25)
# emp1.showInfo()
# emp1.greet()

# emp2 = Manager('aman', 30)
# emp2.showInfo()
# emp2.task()

# public, private A.M. 
# class Employee():
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
    

# emp1 = Employee('rohan', 23)

# print(emp1.__dir__())
# print(emp1._Employee__name)

# Exercise 6: Library Management System 

# class Library:
#     def __init__(self, books):
#         self.books = books
#         self.count = 0
#         print('''
#             Your Library is created, use the following methods:
#               1. print_books() - prints all the books in the library
#               2. count_books() - prints the number of books available
#               3. add_book(book_name) - adds the book to the library
#             NOTE - The books are cleared after the program stops.
#             ''')

#     def print_books(self):
#         print(f'The books present in the library are:')        
#         for i in self.books:
#             print(i, end = ',')

#     def count_books(self):
#         temp_count = 0
#         for i in self.books:
#             temp_count += 1
#         self.count = temp_count
#         print(f'Total Book count is: {self.count}')

#     def add_book(self, book_name):
#         if (book_name not in self.books):
#             self.books.append(book_name)
#             self.count += 1
#             print(f'{book_name} added sucessfully!')
#         else:
#             return f'{book_name} is already present in the library'

# input_books = [
#     "Atomic Habits",
#     "The Psychology of Money",
#     "Rich Dad Poor Dad",
#     "Think and Grow Rich",
#     "The Power of Now",
#     "Deep Work",
#     "The 7 Habits of Highly Effective People",
#     "How to Win Friends and Influence People",
#     "Can't Hurt Me",
#     "Mindset",
#     "The Subtle Art of Not Giving a F*ck",
#     "Ikigai",
#     "The Alchemist",
#     "Start With Why",
#     "The 48 Laws of Power"
# ]

# lib1 = Library(input_books)

# print(lib1.print_books())
# lib1.count_books()

# lib1.add_book('Power of discipline')
# print(lib1.print_books())
# lib1.count_books()

# class Employee:
#     company = 'Meta'
#     no_of_employee = 0

#     def __init__(self, name):
#         self.name = name
#         self.raise_amount = 0.05
#         Employee.no_of_employee += 1
    
#     def show_info(self):
#         print(f'The employee {self.name} works for {self.company} with a raise of {self.raise_amount}')

# emp1 = Employee('rakesh')
# emp1.show_info()

# emp2 = Employee('suresh')
# emp2.company = 'Apple'
# emp2.raise_amount = 0.7
# emp2.show_info()

# Exercise 7 - clear the clutter 

# WAP to clear the clutter. use OS module to rename all the png images -> 1 - n.png,where n is the no. of png files in that folder. DO the same for other file formats. pass the file extension to the function.

# import os

# def clearClutter(fileExtension):

#     def filterExtension(file):
#         if (file.split('.')[1] == fileExtension):
#                 return True
#         return False

#     filePath = "C:\\Users\\username\\Desktop\\Desktop Files\\Desktop Programming Files\\100 days python\\Exercise7"
    

#     listDir = os.listdir(filePath)
#     listExtension = list(filter(filterExtension, listDir))

#     try:
#         for i in range(len(listExtension)):
#             os.rename(f'{filePath}\\{listExtension[i]}', f'{filePath}\\{str(i+1)}.{fileExtension}')
#     except:
#         print('there is something wrong with the file path')
    
# clearClutter('pdf')

# class Employee:
#     company = 'Apple'

#     def show(self):
#         print(f'The person {self.name} works for {self.company}')
    
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany

# emp1 = Employee()
# emp1.name = 'suresh'
# emp1.show()
# emp1.changeCompany('tesla')
# emp1.show()

# print(Employee.company)

# Class Methods as Alternative Constructors 

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def showInfo(self):
#         print(f'The name of the employee is {self.name} and the salary is {self.salary}')
    
#     @classmethod
#     def stringToData(cls, data):
#         name, salary = data.split(' ')
#         return cls(name, salary)
    
# emp1 = Employee('rakhesh', 150000)
# emp1.showInfo()

# emp2Data = 'suresh 160000'
# emp2 = Employee.stringToData(emp2Data)
# emp2.showInfo()


# super keyword 

# class Employee:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
    
#     def parent_method(self):
#         print('This is a Employee parent method')

# class Coder:
#     def parent_method(self):
#         print('This is a CODER parent method')


# class Programmer(Employee, Coder):
#     def __init__(self, name, age, lang):
#         super().__init__(name, age)
#         self.lang = lang
    
#     def child_method(self):
#         super().parent_method()
#         print('This is a child method')

# emp1 = Employee('Rakesh', 23)
# emp1.parent_method()
# print(emp1.name)
# print(emp1.age)

# emp2 = Programmer('suresh', 25, 'Python')
# emp2.child_method()
# print(emp2.lang)


# from Day73_emp import Employee

# emp1 = Employee('rakesh')

# print(len(emp1))
# print(str(emp1))
# print(repr(emp1))
# emp1()

# # factorial of n

# def fact(n):
#     if (n == 0 | n == 1):
#         return 1
#     return n * fact(n-1)

# print(fact(5))
# print(fact(3))

# fibonacci series 

def fibo(n):
    if (n < 0):
        return 'This is a negative number, please provide positive number'
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibo(n-1) + fibo(n-2)

# print(fibo(5))
# print(fibo(6))
# print(fibo(7))

# print fibo series 

def print_fibo(n):
    if (n == 0):
        print(0)
        return

    prev1 = 0
    prev2 = 1

    print(prev1, prev2, end = ' ')

    if (n == 1):
        print()
        return

    for i in range(2, n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
        print(curr, end = ' ')
    print()

# print_fibo(0)
# print_fibo(1)
# print_fibo(2)


# def write_to_file(contents):

#     with open('opening2.txt', 'w') as fs:
#         try:
#             fs.write(contents)
#             return 'File written sucess'
#         except Exception as e:
#             print(e)

# para = 'This is a big para that is used to write to a file using file handling methods'

# print(write_to_file(para))

# def append_to_file(contents):

#     with open('opening2.txt', 'a') as fs:
#         try:
#             fs.write('\n' + contents)
#             return 'File append sucess'
#         except Exception as e:
#             print(e)

# para = 'few additional things that needs to be appended are written here.'

# print(append_to_file(para))

# with open('opening2.txt', 'r') as fs:
#     content = fs.readline().strip('\n')
#     while True:
#         print(content)
#         content = fs.readline().strip('\n')
#         if not content:
#             break

# def append_lines_to_file(content):
#     with open('opening2.txt', 'a') as fs:
        
#         for i in content:
#             fs.write(i + '\n')
        
#         print('Appended new lines to the file')
    
#     with open('opening2.txt', 'r') as fs:
#         content = fs.read()
#         print(content)

# content = ['This is line 1','This is line 2','This is line 3','This is line 4']

# print(append_lines_to_file(content))

# def del_using_seektell():
    
#     contents = ''
#     with open('opening2.txt', 'r') as fs:
#         contents += fs.read(203)
#         fs.seek(205 + 56)
#         contents += fs.read()
#         print(contents)

# res = del_using_seektell()
# print(res)

# List = [Expression(item) for item in iterable if Condition]

# n = 25
# primeL = [i for i in range(2, n+1) if all((i%j != 0) for j in range(2, int(i**0.5+1)))]
# print(primeL)

# class Vector:

#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
    
#     def __str__(self):
#         return f'{self.i}i + {self.j}j + {self.k}k'
    
#     def __add__(self, x):
#         return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
# v1 = Vector(2,5,8)

# v2 = Vector(4, 2, 1)

# print(v1 + v2)
# print(type(v1 + v2))

# Single Inheritance

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def make_sound(self):
#         print('Animal is making the sound')

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species='Dog')
#         self.breed = breed
    
#     def make_sound(self):
#         print('dog is making sound baw')

# a1 = Animal('cat', 'persian')
# a1.make_sound()

# d1 = Dog('Tommy', 'husky')
# d1.make_sound()

# print(Dog.mro())


# Multiple Inheritance

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f'the name of the employee is: {self.name}')
    
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance
    
#     def show(self):
#         print(f'The employee knows {self.dance} dance')

# class EmployeeDancer(Employee, Dancer):
#     def __init__(self, name, dance):
#         self.name = name 
#         self.dance = dance 
    
# o1 = EmployeeDancer('Rahul', 'Free-style')
# o1.show()
# print(EmployeeDancer.mro())

# Time Module 

import time as t

# def whileLoop():
#     i = 0
#     while (i < 1000):
#         print(i)
#         i += 1

# def forLoop():
#     for i in range(1000):
#         print(i)
    

# start_while = t.time()
# whileLoop()
# end_while = t.time()

# start_for = t.time()
# forLoop()
# end_for = t.time()

# print(f'While loop time: {end_while - start_while}')

# print(f'For loop time: {end_for - start_for}')

# print('Hello, the next message will print after 2 seconds')
# t.sleep(2)
# print('goodbye')

# request module

# import requests
# from bs4 import BeautifulSoup

def parse_text():
    URL = 'https://jsonplaceholder.typicode.com/todos/1'

    response = requests.get(URL)

    print(response.text)

# parse_text()

# post request

def post_method():
    URL = 'https://jsonplaceholder.typicode.com/posts'
    
    data = {
        "title": 'foo',
        "body": 'bar',
        "userId": 5
    }

    headers = {
        "Content-type": 'application/json; charset = UTF-8'
    }

    response = requests.post(URL, headers=headers, json=data)
    print(response.text)

# post_method()


def parse_HTML():
    URL = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

    response = requests.get(URL)
    # print(response.text)

    text_format = BeautifulSoup(response.text, 'html.parser')

    try:
        with open('./HTTP_test/google_output.html', 'w') as fs:
            # fs.write(str(text_format.prettify()))
            for words in text_format.find_all('h2'):
                fs.write(str(words) + '\n')
            print('HTML contents written sucess')
    except Exception as e:
        print(e)

# parse_HTML()

def generate():
    for i in range(10):
        yield i

# value = generate()
# print(next(value))
# print(next(value))

# import functools
# import time

# @functools.lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(2)
#     return n*5

# print(fx(5))
# print('Done for 5')
# print(fx(10))
# print('Done for 10')
# print(fx(15))
# print('Done for 15')

# print(fx(5))
# print('Done for 5')
# print(fx(10))
# print('Done for 10')
# print(fx(15))
# print('Done for 15')

# import re

# text = '''
# a Cyclone is a large air mass Dyclone that rotates around a strong center of low atmospheric pressure, Nyclone counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.
# '''

# pattern = r'[A-Z]yclone'

# match_clone = re.findall(pattern, text)
# print(match_clone)

# matches = re.finditer(pattern, text)

# for match in matches:
#     print(match)
#     print(match[0])

# Async programming in python - check async_env folder

import threading, time
from concurrent.futures import ThreadPoolExecutor

def func_sleep(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    return seconds

# time1 = time.perf_counter()
# func_sleep(3)
# func_sleep(2)
# func_sleep(1)
# time2 = time.perf_counter()
# print(time2-time1)

def main():
    time3 = time.perf_counter()

    # make the fn run on different threads
    t1 = threading.Thread(target=func_sleep, args=[3])
    t2 = threading.Thread(target=func_sleep, args=[2])
    t3 = threading.Thread(target=func_sleep, args=[1])

    # start the thread 
    t1.start()
    t2.start()
    t3.start()

    t1.join() # wait until t1 is completed
    t2.join()
    t3.join()

    time4 = time.perf_counter()

    print(time4 - time3)

# using ThreadPoolExecutor for executing multiple tasks

def thread_pool():
    with ThreadPoolExecutor() as executer:
        a = [5,4,3,2,1]
        results = executer.map(func_sleep, a)
        for result in results:
            print(result)

# thread_pool()








