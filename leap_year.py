#define a function checks whether a given year is leap or not.
def leap(start, end):
    leap_year =[]
    for y in range(start, end+1):
        if (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0):
            leap_year.append(y)
    return leap_year   
start = int(input("Enter first year of choice: "))
end = int(input("Enter end year of choice: ")) 
list = leap(start, end)
print(f"The leap years between {start} and {end} are {list}")      
 