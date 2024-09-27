#Notes
''' to remove items you do remove() in a list if there are the same value that are the same i will take out the frist one
if you want to pull out an item form a list but you still want to use it this is done with pop()'''
'''harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]

harvest.remove("squash")
furit = harvest.pop(1)
print(harvest)'''

'''skills = ["Piano", "Soccer", "Coding", "Cooking", "Writing"]
user_input = input("Enter one of these Piano Soccer Coding Cooking Writing ")
skill = skills.remove(user_input)
print(skills)'''

people = input("Enter 3 names separated by spaces: ")

people = people.split()
'''frist = people.pop(0)'''
'''second = people.pop(1)'''
thrid =  people.pop(2)
'''print(frist + " got the gold medal")
print(second + " got the silver medal")'''
print(thrid + " got the bronze medal" )