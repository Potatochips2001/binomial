# px
Binomial probabilites
# usage
replace filename.py with the file name
```sh
chmod +x filename.py
./filename.py
```
# formulas
#### definitions
p = probability <br/>
n = number of trials <br/>
x = Number of successes <br/>
q = 1 - p
### binomial
combinations * p^x * q^(n-x); add up from 0 success all the way to max successes -> basically the sum
### at least x
binomial probabilites from x to n
### at most
sum of 0 to at most number.
### exactly
combinations * p^x * q^(n-x); replace x with exactly number
### less than
same at at least x but subtract 1 from initial x value
### more than
same as less than, but instead of subtracting 1 from initial x value, add one
