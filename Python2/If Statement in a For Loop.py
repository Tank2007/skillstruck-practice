
'''foods = ["mushrooms", "broccoli", "fish", "grape", "kiwi"]

for foods in foods:
   
    if foods == "mushrooms":
        print(foods + " yum.")
    
    
    elif foods == "broccoli":
        print(foods + " yum.")
    
    elif foods == "fish":
        print(foods + " is gross.")
    
    
    else:
        print(foods + " no.")'''

'''my_list = [int(n) for n in input(" Enter 1 to 5 numbers").split()]

for number in my_list:
    if number % 2 == 0:
        print(number, end=' ')'''


# Create a list of integers from input
my_list = [int(n) for n in input().split()]

# Manually calculate the sum of the list
total_sum = 0
for number in my_list:
    total_sum += number

# Calculate the average of the list
count = len(my_list)
average = total_sum / count

# Print numbers greater than the average
for number in my_list:
    if number > average:
        print(number, end=' ')