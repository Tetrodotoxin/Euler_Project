import math

total = 0
for number in range(1,1000):
    is_multiple = False
#    if number%3 == 0:
#        is_multiple = True

    if number%5 == 0:
        is_multiple = True

    if is_multiple:
        total = total + number

print(total)

upper_bound = 999

sum_threes = 3*t(math.floor(upper_bound/3))
print(sum_threes)

sum_fives = 5*t(math.floor(upper_bound/5))
print(sum_fives)

sum_fifteens = 15*t(math.floor(upper_bound/15))
print(sum_fifteens)

print(sum_fives+sum_threes-sum_fifteens)

def t(num):
    return (num*(num+1))/2
