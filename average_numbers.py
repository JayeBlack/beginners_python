print("The Program below finds the average of five numbers in a list where the two lowest numbers are dropped")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#the "numbers" variable stores the user values as list
#where the .format() function makes it user-friendly
numbers = [float(input("Enter number{}:".format(i+1))) for i in range(5)]
sum = 0
average = 0
#the sorted function arranges the numbers in descending order
sorted_list = sorted(numbers,reverse = True)
#the new list excludes the last two numbers
new_list = sorted_list[:-2]

for i in new_list:
    sum += i
    average = sum / len(new_list)
print("******************************************")
print(f"The average number is {average}")    