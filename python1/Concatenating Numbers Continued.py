'''string1 = "Amout of time in scp:sl {} amount of hours I put in scp:sl {}"
hours = 2000
time = 3
print(string1.format(hours, time))'''


#Challenge 1
''''miles_driven_in_one_day = int(input("Number of miles your car can drive in one day: "))
total_miles_to_destintion = int(input("Total number of miles to your destination: "))
number_of_days = total_miles_to_destintion /miles_driven_in_one_day
drive = "The total number of days you will need to drive there is {} "
print(drive.format(number_of_days))'''
#Challenge 2

dollars = int(input("dollars part: "))
cents_part = int(input("cents part: "))
number_to_buy = int(input("How many cookies: "))
cents = cents_part / 100

cost = dollars + cents
total_cost = cost * number_to_buy
string1 = "The total cost of {} cookies is ${}"
print(string1.format(number_to_buy, total_cost))