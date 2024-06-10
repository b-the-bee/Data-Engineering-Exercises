"""Exercises part 2"""

user_integer = int(input("Enter an integer: "))

if user_integer % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")


user_integer = int(input("Enter an integer: "))
if user_integer % 4 == 0:
    print("Your number is divisible by four.")
elif user_integer % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
    
    
user_integer = int(input("Enter an integer: "))

if user_integer % 3 == 0:
    print("fizz")
elif user_integer % 5 == 0:
    print("buzz")

temperature_type = input("Please pick which temperature type you're converting, 'c' for celsius or 'f' for fahrenheit: ").lower()

while temperature_type not in ["c", "f"]:
    print("Please enter c or f")
    temperature_type = input("Please pick which temperature type you're converting, 'c' for celsius or 'f' for fahrenheit: ").lower()

temperature_value = float(input("Please enter the value of the temperature you wish to convert: "))
new_temp_value = 0.1
new_temp_symbol = " "
if temperature_type == "c":
    new_temp_value = (temperature_value * 9/5) + 32
    new_temp_symbol = "f"
else:
    new_temp_value = (temperature_value - 32) * (5/9)
    new_temp_symbol = "c"    
new_temp_value = round(new_temp_value, 2)           


print(f"Your converted temperature is {new_temp_value}{new_temp_symbol}.")                         