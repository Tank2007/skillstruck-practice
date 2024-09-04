'''string1 = "Amout of time in scp:sl {} amount of hours I put in scp:sl {}"
hours = 2000
time = 3
print(string1.format(hours, time))'''


#Challenge 1
miles_driven_in_one_day = int(input("Number of miles your car can drive in one day: "))
total_miles_to_destintion = int(input("Total number of miles to your destination: "))
number_of_days = total_miles_to_destintion /miles_driven_in_one_day
drive = "The total number of days you will need to drive there is {} "
print(drive.format(number_of_days))