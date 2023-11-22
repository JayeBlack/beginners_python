# Define a function to convert weight in kilograms to pounds
def convertWeight():
    try:
        weight = int(input("Enter weight in kilograms:"))
        pounds = weight * 2.20462
        print(f"{weight}kg in pounds is", round(pounds, 1))
    except ValueError:
        print("Please enter a positive number.")    


#define a function to convert temperature in degrees to fahrenheit
def convert_to_fahrenheit():
    try:

        tempt_in_deg = float(input("Temperature in degrees:"))
        tempt_in_fah = (9/5*tempt_in_deg + 32)
        print(f"{tempt_in_deg} degrees celsius in fahrenheit is", round(tempt_in_fah, 1))
    except ValueError:
        print("Please enter an integer value.")
while True:
    print("Select from below what conversion you want:")
    print("1. Convert from degrees to fahrenheit")
    print("2. Convert from kilograms to pounds")
    print("3. Exit")

    choice = input("Enter Your Choice:")
    if choice == "1":
        convert_to_fahrenheit()
    elif choice == "2":
        convertWeight()
    elif choice == "3": 
        break
    else:
        print("Please enter a valid choice")   

    


