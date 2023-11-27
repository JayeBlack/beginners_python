# A program to calculate (1 + 1/2 + 1/3 + ... + 1/{n}) - ln({n})
"""import math
def sum_the_difference():
    n = int(input("Enter Your Number:"))
    total_sum = 0

    for i in range(1,n + 1):
        total_sum += 1/i
    difference = total_sum -math.log(n)
    print(f"The result of (1 + 1/2 + 1/3 + ... + 1/{n}) - ln({n}) is: {difference}")  
sum_the_difference()    
"""
#A program to compute the sum (1 − 2 + 3 − 4 + ··· + 1999 − 2000).

def sum():
    total_sum = 0
    for i in range(1,2001):
        if i % 2 == 0: 
            total_sum -= i
        else:
            total_sum += i
    return total_sum        
result = sum()    
print(f" The sum is {result}")
    