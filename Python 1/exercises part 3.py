# 1
"""
    and check if 2 operations are true, both have to be true in order for the operation to be true
    or checks if either of the 2 operations are true, if 1 is true the operation is true
    not checks if something is not something else, it will output true if they are not
"""
    
# 2

"""
a = False
b = False
x = not(a)
y = not(b)
print(a or b) - False
print(x or y) - True
print(a or x) - True
print(x or b) - True
    
"""

a = False
b = False
x = not(a)
y = not(b)
print(a or b)
print(x or y)
print(a or x)
print(x or b)

# 3 

"""
a = False
b = False
x = not(a)
y = not(b)
print(a and b) - False
print(a and x) - False
print(y and b) - False
print(x and y)- True
    
"""

a = False
b = False
x = not(a)
y = not(b)
print(a and b)
print(a and x)
print(y and b)
print(x and y)

#4 

"""FIRST SECOND OPERATOR OUTPUT
    T       F       and     F
    T       T       and     T
    F       F       and     F
    T       F       or      T
    T       T       or      T
    F       F       or      F
               

"""

#5 

user_age = int(input("Please enter your age: "))
user_salary = int(input("Please enter your salary as a whole number with no commas: "))

if user_age < 21 or user_salary < 21000:
    print("Sorry we cannot offer you a loan right now.")
elif user_age >= 30 and user_salary >= 50000:
    print("We can offer you a loan up to £100 000.")
elif user_age >= 30 and user_salary >= 35000:
    print("We can offer you a loan of up to £75 000.")
elif user_age >= 21 and user_salary >= 21000:
    print("We can offer you a loan of up to £50 000.0.")