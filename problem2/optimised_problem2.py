#PROBLEM 1: Considering the terms in the Fibonacci sequence (starting with 1&2)
# whose values do not exceed four million, find the sum of the even-valued terms.

#SOLUTION LEVEL(optimised): The iterative Fibonacci generator of the first
# version was replaced by a formulaic version derived from the difference
# equations. This poses no real benefit as to find the even values in the series
# we need to compute all values anyway (TODO AJE: IS THIS TRUE???) but it's
# interesting nonetheless!

#COMPLEXITY: O(?) [Assuming the formulaic fib generator holds against rounding
# errors (IT DOESNT AFTER 71 ITERATIONS, see bottom)] TODO AJE: revise

import math

def nth_fib(n):
    root_of_5 = math.sqrt(5)
    fib = round(((1/root_of_5)*(((1+root_of_5)/2)**(n+1)))\
               -((1/root_of_5)*(((1-root_of_5)/2)**(n+1))))
    return fib

n = 1
limit = 4000000
running_total = 0
fib = nth_fib(n)
while fib <= limit:

    if fib%2 == 0: # Is fib even
        running_total += fib

    n += 1
    fib = nth_fib(n)

print("The sum of all even numbers from the Fibonacci sequence not exceeding 4000000 is...")
print(running_total)


### This section is for comparing the formula based Fibonacci generator against
### the iterative one. Because of rounding errors I suspect that the formulaic
### generator will diverge from the integer based iterator. (CONFIRMED: AFTER
### N=71 & FIB>3 TRILLION, THE FORMULAIC GENERATOR DIVERGES BY 1 AFTER ROUNDING)
def fib_gen(num1,num2):
    fib = num1+num2
    return fib

def test_form_fib_gen():
    iter_fib = 1
    old_fib = 0
    n = 1
    form_fib = 1
    while iter_fib == form_fib:

        # iterative fibonacci generator
        new_fib = fib_gen(iter_fib,old_fib)
        old_fib = iter_fib
        iter_fib = new_fib

        # formulaic fibonacci generator
        form_fib = nth_fib(n)
        n += 1

        # print n every 10000 iterations
        if n % 10000 == 0:
            print(n)

        print(n)
    print("DONEZO")
    print(n)
    print(iter_fib)
    print(form_fib)

test_form_fib_gen()#
