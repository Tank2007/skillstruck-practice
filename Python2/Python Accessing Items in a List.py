'''games = ["Victor vran", "Hoi4", "Rb6s", "scp:sl", "rd2", "stardewvally"]

print(games[2])
print("the center game is " + games[2])'''

'''number_list = [int(n) for n in input().split()]

print(number_list[4])
print(number_list * 100)'''



'''number_list = [int(n) for n in input("Enter 9 numbers separated by spaces: ").split()]


if len(my_list) == 9:
 
    center_number = my_list[4]

    
    result = center_number * 100
print(result)'''


my_list = [int(n) for n in input("Input a list of consecutive numbers with some missing: ").split()]


min_num = min(my_list)
max_num = max(my_list)


missing_numbers = [x for x in range(min_num, max_num + 1) if x not in my_list]


missing_numbers.append(max_num + 1)

print(*missing_numbers)
