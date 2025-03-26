'''houses = ["Jon's house", "Kai's House", "astin's house", "evertet's House"]

def deliver_presents_iteratively(houses):
    for house in houses:
        print("Delivering persents to", house)

deliver_presents_iteratively(houses)'''

this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala'] 

'''def feeding(this_list): 
    if len(this_list) == 1: 
        animal = this_list[0]
        print("The " + animal + " has been fed") 
    else:
        mid = len(this_list) // 2 
        first_half = this_list[:mid] 
        second_half = this_list[mid:] 
        feeding(first_half) 
        feeding(second_half) 
        
        
feeding(this_list)'''





'''books = [int(n) for n in input("Input a list of numbers").split()]

def pairs(books):
    if len(books) == 2:
        print(books[0] + books[1])
    else:
        mid = len(books) // 2 
        first_half = books[:mid]
        second_half = books[mid:]

        pairs(first_half)
        pairs(second_half)
pairs(books)'''


'''flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]
def orchard(flowers):
    if len(flowers) == 1:
        print(flowers[0] * 3)
    else:
        mid = len(flowers) // 2
        first_half = flowers[:mid]
        second_half = flowers[mid:]

        orchard(first_half)
        orchard(second_half)
orchard(flowers)'''