import numpy as np


# generate number 0 or 1 with probability 'p' of 1
np.random.seed()
def experiment(numbers, n, p):
    for x in range(0, n):
        c = 0
        i = 0
        while i != 1:
            i = rand_0_or_1(p)
            c += 1
        numbers.append(c)

# rand(p) - returns 0 or 1 with probability p
def rand_0_or_1(probability):
    if np.random.random() > probability:
        return 0
    else:
        return 1

# нахождение медианы в выборке
def findMediana(mass):
    if len(mass)%2 == 0:
        mass.sort()
        return (mass[len(mass)//2] + mass[(len(mass)//2) + 1])/2
    else:
        mass.sort()
        return mass[len(mass)//2] 
    