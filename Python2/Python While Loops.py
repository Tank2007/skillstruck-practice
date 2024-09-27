"""people_in_line = 20
while people_in_line > 0:
    print("there are " + str(people_in_line) + " people in line. Keep the coaster running.")
    people_in_line = people_in_line - 0""" #infinite loop
    #if the 0 was a 1 it would not be an infinite loop and will end.

'''age = 17
while age >= 0:
    print(age)
    age -= 1'''

'''number = 1 
while number <= 49:
    number += 1
    print(number)'''


'''count = 0
user_input = 1
while user_input > 0:
    user_input = int(input("Enter an integer (enter 0 to stop) "))
    
    if user_input == 0:
        break

    count += 1

print(count)'''


total_sum = 0

while True:
    user_input = input("Enter an integer (enter '0' to stop): ")
    
    if user_input == '0':
        break
    
    total_sum += int(user_input)

print(total_sum)
