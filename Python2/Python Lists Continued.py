#notes
'''len(whaterver it is)) this tells you how many items are in a list. indexing start counting at 0 in python. and leaves out the number that is last so like [2:5 the fith itmes will not be inculde. to sort items is sort() in alphabetyically. can also sort numbers.'''

'''games_list = ["scpsl", "hearts of iron iv", "seige", "farcry5", "the finlas", "fallout4", "farcry3"] 

print(games_list[0:3])
games_list[6] = "fallout76"
print(games_list)
print(len(games_list))'''

'''number_list = [int(n) for n in input("Enter numbers with spaces ").split()]
largest_number = number_list[0]

for num in number_list:
    if num > largest_number:
        largest_number = num

print(largest_number)'''


my_list = [int(n) for n in input("Enter numbers separated by spaces: ").split()]


count = 0

for i in range(1, len(my_list) - 1):
    if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
        count += 1

print(count)
