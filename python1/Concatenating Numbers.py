'''string1 = "The number of miles we've hiked toals up to {} which is {} feet."
miles = 21 
feet = 110880
print(string1.format(miles, feet))'''

'''string_variable = "This is a string with curly braces: {}"
integer_variable = 42
print(string_variable.format(integer_variable))'''

#Challenges
age = 16
birthday = "you are {} years old "
print(birthday.format(age))

#Challenge 2
the_users_number = int(input())
hours = the_users_number // 60
minutes = the_users_number % 60
print("It has been {} hour(s) and {} minute(s) since midnight.".format(hours, minutes))