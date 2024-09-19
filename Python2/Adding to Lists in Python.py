'''people = ["dscpo", "drgoanblade"]
people.append("Frankie")
people.extend(["Hugz", "casule"])
people.insert(2, "scp")  
print(people)'''

'''flowers = ["rose", "tulip", "lilac", "sunflower"]
flowers.append("daisy")
flowers.extend(["orchid", "marigold"])
flowers.insert(2, "lily")
print(flowers)'''

'''treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]
user_input1 = input("Enter a treat ")
user_input2 = input("Enter a treat ")
treats.extend([user_input1, user_input2])
print(treats)'''  

user_input = input("Enter a word")
result = []
result.append(user_input)
result.extend(list(user_input))
result.append(user_input)
print(result)