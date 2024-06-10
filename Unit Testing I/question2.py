def add_two_numbers(a, b):
    if isinstance(a, str) or isinstance(b, str):
        a = str(a)
        b = str(b)
        print(a+b)
    else:
        print(a+b)

try:
    add_two_numbers(3, 4)
    add_two_numbers(4, -5)
    add_two_numbers(2.2, 3.2)
    add_two_numbers("one", 2)
    add_two_numbers("string1", "string2")
except TypeError:
    print("Invalid Input")