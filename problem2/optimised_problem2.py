#PROBLEM 2: Considering the terms in the Fibonacci sequence (starting with 1&2)
# whose values do not exceed four million, find the sum of the even-valued terms.

#SOLUTION LEVEL(optimised): The iterative Fibonacci generator of the first
# version was replaced by a formulaic version derived from the difference
# equations. This poses no real benefit as to find the even values in the series
# until you realise that the fibonnaci series by definition follows the pattern
# [odd, odd, even, odd, odd, even] which means instead of operating on every
# integer you need only sum every third.

#COMPLEXITY: O(1/3n) which roughly == O(n), sue me this was tricky [Assuming the
# formulaic fib generator holds against rounding errors (IT DOESNT AFTER 71
# ITERATIONS, see tests at the bottom) ¯\_(ツ)_/¯ ]

import math

def nth_fib(n): # Formulaic calculation of nth fibonnaci number
    root_of_5 = math.sqrt(5)
    fib = round(((1/root_of_5)*(((1+root_of_5)/2)**(n+1)))\
               -((1/root_of_5)*(((1-root_of_5)/2)**(n+1))))
    return fib

n = 2 # Start at n = 2 because we are required to start at where fib == 2 which
      # is the third element.
limit = 4000000
running_total = 0
fib = nth_fib(n)
while fib <= limit:

    running_total += fib
    n += 3 # Because of the pattern of odds and evens in the fibonacci sequence
           # (SEE SOLUTION DESCRIPTION) every third element is even
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

        # Iterative fibonacci generator
        new_fib = fib_gen(iter_fib,old_fib)
        old_fib = iter_fib
        iter_fib = new_fib

        # Formulaic fibonacci generator
        form_fib = nth_fib(n)
        print(form_fib)
        n += 1

        print(n)
    print("DONEZO")
    print(n)
    print(iter_fib)
    print(form_fib)

test_form_fib_gen() #
