'''string1 = "The number of miles we've hiked toals up to {} which is {} feet."
miles = 21 
feet = 110880
print(string1.format(miles, feet))'''

'''string_variable = "This is a string with curly braces: {}"
integer_variable = 42
print(string_variable.format(integer_variable))'''

#Challenges
'''age = 16
birthday = "you are {} years old "
print(birthday.format(age))'''

# #Challenge 2
# the_users_number = int(input())
# hours = the_users_number // 60
# minutes = the_users_number % 60
# print("It has been {} hour(s) and {} minute(s) since midnight.".format(hours, minutes))

dollars = int(input("dollars part: "))
cents_part = int(input("cents part: "))
number_to_buy = int(input("How many cookies: "))
cents = cents_part / 100

cost = dollars + cents
total_cost = cost * number_to_buy
string1 = "The total cost of {} cookies is ${}"
print(string1.format(number_to_buy, total_cost))