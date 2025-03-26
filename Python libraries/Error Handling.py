''' The try block Tests a code for errors

The except block Code to run if an error happens

The else block Code to run if no error happens

The finally block Code to run regardless of the try/except blocks.'''

'''greeting = "hallo"

try:
    print(greeting)
except:
    print("A problem occurred")
else:
    print("The code worked without a problem ")
finally:
    print("Your exception handling is complete")'''
    



'''pizza_slices = (input("How many slices of pizza do you need: "))

people = (input("Enter the number of people at the party: "))

try:
    slices_per_person = pizza_slices // people  
    print(f"Each person gets {slices_per_person} slice(s).")
except:
    print("Your code doesn't account for if a user tries to enter 0 people.")
else:
    print("There is no problem.")
finally:
    print("Your exception handling is complete.")'''

'''sunflower_seeds = 300 
sunflower = int(input("Enter the amount of sunflowers: "))

try:
    seeds_per_flower = sunflower * sunflower_seeds 
    print(f"number of sunflowers seeds {seeds_per_flower}")
except: 
    print("There is a problem")
else:
    ("There is no problem")
finally:
    print("Your exception handling is complete")'''