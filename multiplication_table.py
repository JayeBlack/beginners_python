user = int(input("Enter number to find its multiplication:"))
end = int(input("To what length do you wish to end:"))
for i in range(1, end + 1):
    print(user, "x", i, "=", user * i)
