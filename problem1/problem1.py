#PROBLEM 1: If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
# all the multiples of 3 or 5 below 1000.

#SOLUTION LEVEL(simple): for each number between 1 & 1000 check to see if it is
# divisible by 3 or 5. if so add it to a running total to find the sum.

import math

total = 0 #Initialize running count
for number in range(1,1000): #For each integer below 1000
    is_multiple = False
    if number%3 == 0: #If 'number' is divisible by 3 set 'is_multiple' flag true
        is_multiple = True

    if number%5 == 0: #Same as before but due to flag there will be no double
                      # counting if number is divisible by 3 and 5
        is_multiple = True

    if is_multiple:
        total = total + number #The running total is the answer!

print("The sum of all numbers below 1000 that are divisible by 3 or 5 is...")
print(total)
