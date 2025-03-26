'''import datetime
x = datetime.date.today()
print(x)'''

'''# Local Time 
import datetime
x = datetime.datetime.now()
print(x.strftime("%X"))



# 2 digit Month
import datetime
x = datetime.datetime.now()
print(x.strftime("%m"))


# 2 Digit Day 
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))


# 4 digit Year 
import datetime 
x = datetime.datetime.now()
print(x.strftime("%Y"))'''



#all of the times of day or most of them 
# %a Weekday short exp Thurs 
# %A Weekday long Thursday
# %b Month short Sept 
# %B Month long September
# %y 2 Digit Year 25
# %M Minute 35
# %S Second 30 

'''import datetime 
today = datetime.date.today()
x = datetime.datetime.now()
print(x.strftime("%X"))
print(x.strftime("%m"))
print(x.strftime("%d"))
print(x.strftime("%Y"))
print(today)'''

'''import datetime 
x = datetime.datetime.now()
y = (int(x.strftime("%Y")) - 1972)
print(f"It has been {y} years since the first computer program ever. Look how far we have come!")'''

'''import datetime
x = datetime.datetime.now()
time = (int(x.strftime("%Y")) - 2020)'''

'''import datetime
x = datetime.datetime.now()
current_year = x.year  # Extract the year
time = current_year - 2020  # Calculate difference from 2020
calculation = time % 4  # Check if divisible by 4
if calculation == 0:
    print(f"This year {current_year}, is a leap year")
else:
    print(f"This year {current_year}, is not a leap year")'''

