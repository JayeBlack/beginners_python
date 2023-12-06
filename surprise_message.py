from random import randint


def guess_a_number():
    scores = 0
    message = "Hey, you mean a lot to me"

    numbers = randint(1, 10)
    for _ in range(5):
        user = int(input("Guess a number(1-10):"))

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
        message = message[::-1]
        print(message)
    else:
        print("Better luck next time.")


guess_a_number()
