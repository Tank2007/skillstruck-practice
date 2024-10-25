''' this is how you make a 1d list 
n = 5 
list = []
for i in range(n):
    list.append(i)
print(list)'''

'''this is how you make a 2d list 
rows = 5 
cols = 5 
list = [] 
for i in range(cols):
    col = []
    for j in range (rows):
        col.append(j)
    list.append(col)
print(list)'''



'''rows = 3  
pets = ["dog", "cat", "bird", "fish", "hamster"]

pets_list = [[pet for pet in pets] for _ in range(rows)]

print(pets_list)'''

'''rows = input("how many rows do you want to print")
my_list= input("put in 5 numbers")

mylist_list = [[my_list for my_list in my_list] for _ in range(rows)]
print(my_list)'''

'''rows = int(input("How many rows do you want to print? "))
mylist = [1, 2, 3, 4, 5]

mylist_2D = [[num * rows for num in mylist] for _ in range(rows)]

print(mylist_2D)'''



rows = input("Input a list of weather: ").split()

cols = ["windy", "breezy", "calm"]

weather_wind = [[f"{weather} {wind}" for wind in cols] for weather in rows]

print(weather_wind)
