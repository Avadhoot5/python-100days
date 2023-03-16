# Walrus Operator -  it allows you to assign a value to a variable within an expression 
print(a:= False)

numbers = [1,2,3,4,5,6]

while (n := len(numbers)) > 0:
    print(numbers.pop())

# Walrus operator use case 
# foods = list()
# while True:
#     food = input("Enter your favourite game: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods =  list()
while (food := input("Enter your favourite game: ")) != "quit":
    foods.append(food)
# print(foods)