#define a function that calculates the factorial of a number
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter a number:"))
result = factorial(number)
print(f"The factorial of {number} is: {result}")  