
def add_two_numbers(a, b):
    c = a + b
    print(c)
    
    
try:
    add_two_numbers(1, 2)
    add_two_numbers(2.3, 2.4)
    add_two_numbers(1.7, -1.9)
    add_two_numbers("one", 2)
except Exception as e:
    print(e)
    print("Invalid input")
    