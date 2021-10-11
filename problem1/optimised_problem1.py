#PROBLEM 1: If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
# all the multiples of 3 or 5 below 1000.

#SOLUTION LEVEL(optimised): for each divisor the "floored" division of the
# target_num by the divisor gives you the amount of elements that are multiples.
# An example of the set of multiples; [3,6,9,12,15,18...999]. To sum these
# consider that (3+6+9+...999) is equivalent to 3*(1+2+3+...333). The solution
# the series (1+2+3+...n) otherwise known as the "nth triangle number" is
# "(n**2 + n)/2". So to generalise, the solution the sum of all multiples of 'n'
# below number 't' is the n * the "triangle number" of "floor(t/n)". Next we
# take the sums of n=3 plus n=5 and minus n=15 to deduplicate common factors of
# 3 & 5.

#COMPLEXITY: O(1)

import math

def get_triangle_number(n):# the nth triangle number is the sum of 1 to n
    sum = ((n**2) + n)/2
    return sum

target_num = 999 # "Below" 1000
# Find the number of multiples
num_multiples_of_3 = math.floor(target_num/3)
num_multiples_of_5 = math.floor(target_num/5)
num_multiples_of_both_3_and_5 = math.floor(target_num/15)

# Find the sum of those multiples using the triangle number
sum_multiples_of_3 = 3 * get_triangle_number(num_multiples_of_3)
sum_multiples_of_5 = 5 * get_triangle_number(num_multiples_of_5)
sum_multiples_of_both_3_and_5 = 15 * get_triangle_number(num_multiples_of_both_3_and_5)

total = sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_both_3_and_5

print("The sum of all numbers below 1000 that are divisible by 3 or 5 is...")
print(total)
