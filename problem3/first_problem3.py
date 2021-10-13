#PROBLEM 3: What is the largest prime factor of the number 600851475143?

#SOLUTION LEVEL(simple):

#COMPLEXITY: O(?)

def isPrime(num):
    is_prime = True
    for it in range(2,num): #prime only has factors 1 and itself
        if num%it == 0:
            is_prime = False
            break
    return is_prime

import math

num = 600851475143

sqrt_num =  math.sqrt(num)
factor = 0
larg_prime_fact = 1
