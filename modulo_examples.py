#define a function that finds the mod of a particular number. Example: 12 mod 7
def mod_of_a_number():
    try:
        number = int(input("Enter a dividend:"))
        mod = int(input("Enter a divisor:"))
        result = number%mod    
        print(f"{number} modulo {mod} is: {result} ")
    except ValueError:
        print("Invalid input. Please enter an integer")    

# Define a function to calculate the last digit of m raised to a power.
def last_digit():
    try:
        num = int(input("Enter a base number:"))
        power = int(input("Enter your power: "))  
        result= num**power
        print(f"The last digit of {num}^{power} is {result%10}")
    except ValueError:
        print("Invalid input. Please enter an integer")     

# Define a function to calculate the last two digits of a known base raised to a power
def last_two_digits():
    try:
        power = int(input("Enter your power: "))  
        result = 4**power
        print(f"The last two digit of 4^{power} is {result%100}")

    except ValueError:
        print("Invalid input. Please enter an integer" )    

# Define a function to calculate the last n digits of m raised to a power
def last_n_digits():
    try:
        num = int(input("Enter a base number:"))
        power = int(input("Enter a power: "))
        digits = int(input("Enter the number of digits you want: "))
       
        while digits < 0:
            print("Invalid input. Please enter a positive value for digits.")
            digits = int(input("Enter the number of digits you want: "))

        result = pow(2, power) % pow(10, digits)

        print(f"The last {digits} digits of {num}^{power} are: {result}")

    except ValueError:
        print("Invalid input. Please enter an integer ")

# Main program loop
while True:
    # Display a menu of options for the user
    print("**********************************************")
    print("*                                            *")
    print("* This program serves as a modulo calculator *")
    print("*                                            *")
    print("**********************************************")
    print("Select from below a function to use:")
    print("1. Mod of a number")
    print("2. Last digit of m exponent n")
    print("3. Last two digits of m exponent n")
    print("4. Last unknown digit(s) of m exponent n")
    print("5. Exit")

    # Prompt the user to enter a choice
    choice = input("Enter your choice function:")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        mod_of_a_number()

    elif choice == "2":
        last_digit()
    elif choice == "3":
        last_two_digits()
    elif choice == "4":
        last_n_digits()
    elif choice == "5":
        break
    else:
        print("Please enter a valid choice.")