#!/usr/bin/env python3

from math import *
import sys

if len(sys.argv) < 2:
    uiP = float(input("Probability: "))
    uiN = int(input("Trials: "))
    uiX = int(input("Successes: "))
elif str(sys.argv[1]).lower() == '-h' or str(sys.argv[1]).lower() == '--help':
    exit(f'{__file__} p n x')
else:
    uiP = float(sys.argv[1])
    uiN = int(sys.argv[2])
    uiX = int(sys.argv[3])

sums = []

def getCombinations(n, x):
    combinations = ( factorial(n) / ( factorial(x) * factorial(n-x) ) )
    return combinations

def getBinomial(p, n, x):
    combinations = getCombinations(n,x)
    q = 1 - p
    return combinations * p**x * q**(n-x)

probability = getBinomial(uiP, uiN, uiX)

print(probability)
