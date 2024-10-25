''' for loops list 
n = 5 
list = []
for i in range(n):
    list.append(0)
print(list)'''

'''rows = 5
cols = 3

list_2d = []

for i in range(rows):
    for j in range(cols):
        rows.append(5)  
    list_2d.append(rows)  
print(list_2d)'''


'''flavors = ["apple", "grape", "peach", "cinnamon", "vanilla"]

fruits = input("Input a list of fruits: ").split()


combined_list = [[fruit + " " + flavor for flavor in flavors] for fruit in fruits]

print(combined_list)'''

'''cols = [2, 5, 10, 100]

rows = [int(n) for n in input("Input a list of numbers: ").split()]

result = [[row - col for col in cols] for row in rows]

print(result)'''

