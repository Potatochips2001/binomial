#!/usr/bin/env python3

from math import *
import sys

if len(sys.argv) <= 2:
    uiP = float(input("Probability: "))
    uiN = int(input("Trials: "))
    uiX = int(input("Successes: "))
elif str(sys.argv[1]).lower() == '-h' or str(sys.argv[1]).lower() == '--help':
    exit(f'{__file__} p n x')
else:
    uiP = float(sys.argv[1])
    uiN = int(sys.argv[2])
    uiX = int(sys.argv[3])

def getCombinations(n, x):
    combinations = (factorial(n)) / (factorial(x) * factorial(n-x))
    return combinations
def getBinomial(p,n,x):
    combinations = getCombinations(n, x)
    q = 1 - p
    return combinations * p**x * q**(n-x)

sums = []
probability = 0

for i in range(0, uiX+1):
    sums.append(getBinomial(uiP, uiN, i))
for i in range(len(sums)):
    probability += sums[i]

print(probability)
