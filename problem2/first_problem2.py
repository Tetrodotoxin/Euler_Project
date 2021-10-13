#PROBLEM 2: Considering the terms in the Fibonacci sequence (starting with 1&2)
# whose values do not exceed four million, find the sum of the even-valued terms.

#SOLUTION LEVEL(simple): For each value made by the iterative fibonacci
# generator, if it is divisible by 2, add it to the running_total.

#COMPLEXITY: O(n)

def fib_gen(num1,num2):
    fib = num1+num2
    return fib

running_total = 0
limit = 4000000
# Ininitialize fibonacci values
fib = 2
old_fib = 1

while fib <= limit:

    if fib%2 == 0: # Is fib even
        running_total += fib

    new_fib = fib_gen(fib,old_fib)
    old_fib = fib
    fib = new_fib

print("The sum of all even numbers from the Fibonacci sequence not exceeding 4000000 is...")
print(running_total)
