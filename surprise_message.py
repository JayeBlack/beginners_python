from random import randint


def guess_a_number():
    scores = 0
    message = "em ot tol a naem uoY"
    try:
        name = input("Hello there! Tell us your name:")
    except ValueError:
        print("Please enter your name:")    
    numbers = randint(1, 10)
    for _ in range(5):
        try:
            user = int(input("Guess a number(1-10):"))
        except ValueError:
            print("Please enter a number(1-7)")
        if user == numbers:
            print("You guessed the number correctly!")
            scores += 10
        else:
            print("Your guess was wrong.")
            scores -= 1
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(f"Your total score is {scores}")

    if scores >= 1:
        print("Congratulations! You've unlocked a surprise message.")
        print(f"{name}",message)
    else:
        print("Better luck next time.")


guess_a_number()
