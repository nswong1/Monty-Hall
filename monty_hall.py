import random

#possible choices
choices = ['car', 'goat', 'goat']
random.shuffle(choices)


print("Choose one of these three doors, behind one of the doors is a brand spanking new car, behind the other two are goats")
choice = int(input("Pick one of the doors 1,2,3: "))


#finds the door to open that isn't car
goat_door = choices.index('goat')
print(goat_door+1)
if choice == (goat_door+1):
    if choices.index('car') == 0:
        goat_door = 3
    elif (choices.index('car') == 1) and (choice == 1):
        goat_door = 3
    elif (choices.index('car') == 2) and (choice == 1):
        goat_door = 2
    elif (choices.index('car') == 2) and (choice == 2):
        goat_door = 1
else:
    goat_door += 1

print(f"Well well, I know what's behind each door and I choose to open door #{goat_door}")



switch = input("Do you decide to switch your answer? ").lower()

if switch == 'yes':
    valid_choice = 0
    valid = False
    while not valid:
        valid_choice += 1
        if valid_choice != choice and valid_choice != goat_door:
            valid = True

if switch == 'yes':
    print(f'You chose door #{valid_choice} and got yourself a {choices[valid_choice-1]}')
else:
    print(f'You chose door #{choice} and got yourself a {choices[choice-1]}')

