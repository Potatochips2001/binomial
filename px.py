#!/usr/bin/env python3
from math import *
import sys

sums = []

def getCombinations(n, x):
  combinations = ( factorial(n) ) / ( factorial(x) * factorial( n - x ) )
  return combinations

def getBinomial(p, n, x):
  combinations = getCombinations(n, x)
  q = 1 - p
  return combinations * p**x * q**(n-x)

if len(sys.argv)<2:
  uiP = float(input("P="))
  uiN = int(input("n="))
  uiX = int(input("x="))
elif str(sys.argv[1]).lower() == '--help' or str(sys.argv[1].lower()) == '-h':
  exit('./px.py p n x')
else:
  uiP = float(sys.argv[1])
  uiN = int(sys.argv[2])
  uiX = int(sys.argv[3])

for i in range(uiX, uiN+1):
  sums.append(getBinomial(uiP, uiN, i))


probability = 0
for i in range(len(sums)):
  probability += sums[i]

print(f"P={probability}")
