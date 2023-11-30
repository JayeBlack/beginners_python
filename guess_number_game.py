from random import randint

def guess_game():
    scores = 0
    
    for _ in range(3):
        try:
            user = int(input("Guess a number between 1 and 10:"))
        except ValueError:
            print("Please enter a number")
            continue    
        random_num =randint(1, 10)
        if user == random_num:
            print("Your Guess was correct!", )
            scores += 10
            
        else:
            print("Incorrect guess. Try again")
            scores -= 1
    
    print(f"Game over!. Your final scores is {scores}")

guess_game()