# This Python code generates and prints the squares of numbers from 1 to 100.
# Additionally, it keeps track of the count of squares that are multiples of 10
count = []
for i in range(1, 101):
    print(i**2)
    if i % 10 == 0:
        count.append(i)

print(f"The number of squares in 1 to 100 that are multiples of 10 are {count}")

# A program that counts how many of the squares of the numbers from 1 to 100 end in a
# 4 and how many end in a 9.
print("************************************************************************************************")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("                                                                                                ")
print("************************************************************************************************")

count1 = []
count2 = []
for i in range(1, 101):
    print(i**2)
    if i % 10 == 4:
        count1.append(i)
    elif i % 10 == 9:
        count2.append(i)

print(f"number of squares in ending in 4s are {count1} and that of 9s are {count2}")


#A program to calculate the sum of the squares within a range
sum = 0
first_num = int(input("Enter your first number:"))
second_num = int(input("Enter your second number:"))
for i in range(first_num, second_num+1):
    squares = i**2
    sum +=squares
print(f"The sum of the squares between {first_num} and {second_num} is {sum}")

