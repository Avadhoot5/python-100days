# Exericse 3: Solution to KBC

# storing ques and their correct ans in a list, correct ans will be checked with negative indexing

questions = [
    ["What is the Capital of India", "mumbai", "nagpur", "delhi", "kolkata", 3],
    ["Who is the current Prime Minister of India", "Salman Khan", "Nardendra Modi", "Kapil Sharma", "Akshay Kumar", 2],
    ["Which is the parent company of WhatsApp", "Instagram", "Tiktok", "Google", "Meta", 4],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
    ["Which is the parent company of Google", "Instagram", "Tiktok", "Alphabet", "Meta", 3],
]

print("Welcome to KBC")

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0,len(questions)):
    question = questions[i]
    a = levels[i]
    print(f"Question fo Rupees {a}\n") 
    
    for i in range(1):
        print(question[i])
    
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    
    ans = int(input("Enter your ans (1-4): "))
    print("Please enter the response in numbers")
    
    print(question[-1])

    if(ans != question[-1]):
        print("Wrong answer")
        break
    else:
        print(f"Correct answer, your amount is {a}")
    



