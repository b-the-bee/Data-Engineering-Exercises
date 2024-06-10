# 1
import math

print(math.factorial(9))

# 2

from math import factorial

print(factorial(10))

# 3
from module_one import factorial_func

print(factorial_func(12))

"""
Variable Scope:
1. a and b are local to the function my_function, 
c and d are global (d is only defined in the case of the 
if statement being true)
2. 
"""

x = "Status"

print (x)