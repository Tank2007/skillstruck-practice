'''coins = 10 
if coins > 20:
    print("ou have more than enough to buy a puppy")
elif coins == 20:
    print("You have exactly enough to buy a puppy")
else:
    print("You do not have enough to buy a puppy")'''

'''user_input1 = int(input("Enter a number "))
user_input2 = int(input("Enter a another number "))

if user_input1 > user_input2:
    print("The first number is larger.")
elif user_input2 > user_input1:
    print("The second number is larger.")
elif user_input1 == user_input2:
    print("The numbers are the same.")'''

user_input1 = input("Enter your frist number ") 
user_input2 = input("Enter your sencend number ")
user_input3 = input("Enter your thrid number ")

if user_input1 == user_input2 == user_input3:
    print("3")
elif user_input1 == user_input2 or user_input1 == user_input3 or user_input2 == user_input3:
    print("2")
else:
    print("0")