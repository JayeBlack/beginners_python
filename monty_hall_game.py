import random

print("**********************************************")
print("*            MONTY HALL GAME🎁🎁             *")
print("**********************************************")
user_name = input("Please enter your name:")
print(f"Hello {user_name}! You are welcome to monty hall game.")


def monty_hall():
    doors = [1, 2, 3, 4]
    spare = doors.copy()
    car_door = random.choice(doors)
    _ = doors.pop(doors.index(car_door))
    user_choice = int(input("Choose a door(1,2,3 or 4):"))
    goats = [door for door in doors if door != user_choice]
    monty_opens = random.choice(goats)
    remaining_for_user = [door for door in spare if door != user_choice and door != monty_opens]
    remaining_wrong_doors = [door for door in doors if door != car_door and door != monty_opens]
    monty_trick = random.choice(remaining_wrong_doors)
    while user_choice not in doors:
        print("Please enter a number {1,2,3 or 4}")
        user_choice = int(input("Choose a door(1,2,3 or 4):"))
    print(f"You have chosen door {user_choice}.")
    if user_choice in goats:
        print(f"Before we proceed, door {monty_trick} has a goat behind it. ")
    else:
        print(f"Before we proceed, door {monty_opens} has a goat behind it. ")

    print("Do you want to stand by your decision or change your choice?")
    decision = input("Enter 'Yes' to stand by your initial decision and 'No' to change:").lower()

    if decision == "yes":
        if user_choice == car_door:
            print(f"{car_door} was the right choice!")
            print("Congratulations! You've unlocked a car 🎉🎊✨")
        else:
            print("Sorry, you chose a wrong door.")
            print(f"The correct door was {car_door}")

    elif decision == "no":
        print(f"Doors {user_choice} and {monty_opens} are out. You are left with doors {remaining_for_user}")
        final_choice = int(input(f"Choose one of the doors {remaining_for_user}:"))
        if final_choice == car_door:
            print(f"Door {car_door} was the right choice!")
            print("Congratulations! You've unlocked a car 🎉🎊✨")
        else:
            print("Sorry, you chose a wrong door.")
            print(f"The correct door was {car_door}.")


monty_hall()
