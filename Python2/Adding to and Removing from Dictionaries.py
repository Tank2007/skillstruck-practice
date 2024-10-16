# to add things in a dictionaries 
'''games = {} 
games["scp:sl"] = 1
games["r6"] = 2

print(games)'''
# to remove something 
'''games = {
    "scp:sl" : 1,
    "R6" : 2, 
    "fallout76" : 3,
}
print(games)

games.pop("fallout76")

print(games)'''

'''friends = { 
    "Shane" : 10, 
    "Samantha" : 9, 
    "Shiloh" : 12, 
    "Sean" : 11 
}
friends = {}

friends["Sebastian"] = 8

print(friends)

friends.pop("Shiloh")'''

'''userinput = input("What tree do you want to get rid of aspen, pine, maple, oak, willow, cottnwood")

trees = { "aspen" : 75, "pine" : 82, "maple" : 60, "oak" : 65, "willow" : 80, "cottonwood" : 100 }

trees.pop(userinput)
print(trees)'''

userinput = input("what goal do you want to get rid of piano, run, paint, serve, homework")

goals = { 
    "piano" : 5, 
    "run" : 3, 
    "paint" : 2, 
    "serve" : 7, 
    "homework" : 7
}

goals.pop(userinput)
print(goals)