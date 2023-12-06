def balance(expression):
    count = 0

    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

    return count == 0


user = input("Enter an expression:")
result = balance(user)
if result:
    print("Your parenthesis are balanced")
else:
    print("Your parenthesis aren't balanced")
