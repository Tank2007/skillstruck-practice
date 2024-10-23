'''classmates = {
    "billy" : 8,
    "Vance" : 15,
    "Alice" : 10,
    "lily" : 6,
    "Xavier" : 12
}

print(len(classmates))


coins = {
    "pennies" : 2,
    "niclels" : 5,
    "dimes" : 10,
    "quarters" : 4
}

coins["silver_dollar"] = 0
coins.pop("pennies") 
print(coins)
print(len(coins))'''



#Challenges 
'''work = {
    "Monday" : 3,
    "Tuesday" : 6,
    "Wednesday" : 6,
    "Thursday" : 6,
    "Friday" : 6,
    "Saterday" : 6,
    "Sunday" : 0
}
 
work["Saturday"] = 7
work.pop("Wednesday")
print(len(work))
if "Friday" in work:
    print("Friday is in dictionary")
print(work)'''

names = [str(n) for n in input("Input a list of names separated by spaces").split()] 
name_dict = {name: "yes" for name in names}

print(name_dict)
