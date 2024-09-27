'''def race():
    print("jon won the race")

race()
print(race)'''

'''def charlie():
    print("W")

charlie()
print(charlie)'''


def game():
    user_input = input("Do you want to start the game? (yes/no): ")
    
    if user_input.lower() == 'yes':
        print("Initialization Complete")
    else:
        print("Initialization Failed")

game()