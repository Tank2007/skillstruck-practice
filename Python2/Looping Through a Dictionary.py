'''games = {
    "scp:sl" : 1,
    "fallout4" : 2
}
for x in games:
    print(x)
#this will print out the keys to print values it is for x in blank.values(): enter print(x) to print both out for x,y in blank.items(): enter print(x,y)'''

'''measurement = { 
    "length" : 3,
    "width" : 7,
    "depth" : 6
}
for value in measurement.values():
    print(value)'''

'''group = {
    "Fred": 12,
    "Jackson": 15,
    "Sophie": 20,
    "Amanda": None,  
    "Jane": None
}


group["Amanda"] = int(input("How many people will Amanda bring? "))
group["Jane"] = int(input("How many people will Jane bring? "))

total_people = 0

for value in group.values():
    total_people += value

print(total_people)'''



'''group = { 3 : 10,
    5 : 3,
    10 : 6,
    4 : 30,
    "temp" : None,
    "temp2" : None }




group["temp"] = int(input("Enter a number: "))
group["temp2"] = int(input("Enter a number again: "))

total_number = 1 
for value in group.values():
    total_number = group["temp"] * group["temp2"]
print(total_number)'''




group = { 
    "Sally": 10, 
    "Cameron": 3, 
    "Spencer": 6, 
    "temp_key": None 
}

new_key = input("Enter the name for the last person: ")
new_value = int(input(f"How many pairs of shoes does {new_key} have? "))

group["temp_key"] = new_key
group[new_key] = new_value


for key, value in group.items():
    if key != "temp_key":  # Skip the temp_key
        print(f"{key} has {value} pairs of shoes.")
