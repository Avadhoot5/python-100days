# Exercicse 3: KBC ques
# create a list to store the ques and their correct ans. display the final amount the person is taking home after playing the game.

# KBC GAME
'''
Greet screen to kbc
rules: 1k points for every correct ans, if wrong ans then game ends.
    variable is True until the ans are right, var gets false and exits the loop.
QUES variable in list - consists of below ques
    Q1, Q2, Q3... Q10
list of ques range(11)
list of answers in another list -- check them -- if this exists in this  
increment points for every correct ans
break the loop if wrong ans.
display the winning price at the end.
thanks for playing
'''

# name = input("Hello, Please Enter Your Name: ")
# print(name.capitalize(), "Welcome to KBC")
print('''
Here are the Rules for the Game:
    1. For every correct answer you will be credited with 1,000 points
    2. But if you provide a wrong answer you'll lose the game, and win the amount for correct answer only. 
ALL THE BEST
''')


# question = []
# for i in range(4):
#     qseries = 'q' + str(i+1)
#     question.append(qseries)
# print(question)


# for i in question:

# Earlier code not working

# q1 = ["mumbai", "nagpur", "delhi", "kolkata"]
# q2 = ["Salman Khan", "Nardendra Modi", "Kapil Sharma", "Akshay Kumar"]
# q3 = ["Instagram", "Tiktok", "Google", "Meta"]
# q4 = ["Instagram", "Tiktok", "Alphabet", "Meta"]

# answer = True
# points = 0

# if(answer):
#     print("What is the Capital of India\n", q1)
#     ans1 = input("Enter Your Anwer: ")
#     if(ans1 == (q1[2])):
#         points()
#     print("Who is the current Prime Minister of India\n", q2)
#     ans2 = input("Enter Your Anwer: ")
#     if(ans2 == (q2[1])):
#         points()
#     print("Which is the parent company of WhatsApp\n", q3)
#     ans3 = input("Enter Your Anwer: ")
#     if(ans3 == (q3[3])):
#         points()
#     print("Which is the parent company of Google\n", q4)
#     ans4 = input("Enter Your Anwer: ")
#     if(ans4 == (q4[2])):
#         points()
# else:
#     print("You lost all points")

# # function to increment points for each correct answer 

# def points():
#     if(answer):
#         points = points + 1000
#     return points

# TEST CODE WORKING


q1 = ["mumbai", "nagpur", "delhi", "kolkata"]
q2 = ["Salman Khan", "Narendra Modi", "Kapil Sharma", "Akshay Kumar"]
q3 = ["Instagram", "Tiktok", "Google", "Meta"]
q4 = ["Instagram", "Tiktok", "Alphabet", "Meta"]

answer = True

# def points():
#      global point
#      point = 0
#      point = point + 1000
#      return point

if(answer):
     print("What is the Capital of India\n", q1)
     ans1 = input("Enter Your Anwer: ")
     if(ans1 == (q1[2])):
          point = 1000
          print("Next Ques\n")
     elif(ans1 != (q1[2])):
          print("Wrong answer")
          point = 0
          print(point)
     print("Who is the current Prime Minister of India\n", q2)
     ans2 = input("Enter Your Anwer: ")
     if(ans2 == (q2[1])):
          point = point + 1000
          print("Next Ques\n")
     elif(ans2 != (q2[1])):
          print("Wrong answer")
          print(point)
     print("Which is the parent company of WhatsApp\n", q3)
     ans3 = input("Enter Your Anwer: ")
     if(ans3 == (q3[3])):
          point = point + 1000
          print("Next Ques\n")
     elif(ans3 != (q3[3])):
          print("Wrong answer")
          print(point)
     print("Which is the parent company of Google\n", q4)
     ans4 = input("Enter Your Anwer: ")
     if(ans4 == (q4[2])):
          point = point + 1000
          print("Congrats you won", point)
     elif(ans4 != (q4[2])):
          print("Wrong answer")
          print(point)

if((ans1 != (q1[2])) or (ans2 != (q2[1])) or (ans3 != (q3[3])) or (ans4 != (q4[2]))):
     print("Thanks for Playing")
