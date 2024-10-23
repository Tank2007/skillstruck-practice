
+'''classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
    "Eliza" : 15,
    "Xavier" : 6,
}

for x in classmates:
    if x == "Eliza":
        print("This person wants to be anonymous")
    else:
            print(x)'''

'''ride = { 
    "Billy" : 100,
    "Vance" : 200,
     "Alice" : 300,
     "Eliza" : 400,
     "Xavier" : 99,
}

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
    else:
        print ("This person is too short to ride.")'''
    

'''dictionary = {7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth"}

my_list = [int(n) for n in input().split()]

for number in my_list:
    if number in dictionary:
        print("Yes")
    else:
        print("No")'''



words = input("Enter a list of words separated by spaces: ").split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = ""
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print(most_frequent_word)
