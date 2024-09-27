'''def weather(forecast):
    print("It's a soggy day outside because it is" + forecast)

weather("raining")
weather("snowing")
weather("drizzling")'''



'''fruit = input("Enter a type of fruit ")

def food(fruit_name):
    print(fruit_name * 3)

food(fruit)'''

'''def days_in_months(month):

   if month == 1:
       print(31)
    elif month == 2:
        print(28)
    elif month == 3:
        print(31)
    elif month == 4:
        print(30)
    elif month == 5:
        print(31)
    elif month == 6:
        print(30)
    elif month == 7:
        print(31)
    elif month == 8:
        print(31) 
    elif  month == 9:
        print(30)
    elif month == 10:
        print(31)
    elif month == 11:
        print(30)
    else:
         month == 12:
        print(31)'''
    
def circle_area(radius):
    area = 3.14159 * radius * radius
    print(f"{round(area, 1)}")

radius_input = float(input("Enter the radius of the circle: "))

circle_area(radius_input)