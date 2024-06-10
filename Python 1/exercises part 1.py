# first_name = "Sam"
# last_name = "Brunkard"

# print(f"Hi my name is {first_name} {last_name}.")


# first_integer = 23
# second_integer = 32
# product_of_two = first_integer * second_integer

# print(f"The product of {first_integer} and {second_integer} is {product_of_two}.")

# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# print(people[2])
# print(people[-2])
# new_people = people[2:6]
# print(people[0] == people[-1])


# user_name = input("What is your name please")
# print(f"Your name is {user_name}.")



user_integer_one = int(input("What is your first integer?"))
user_integer_two = int(input("What is your second integer?"))
user_integer_product = user_integer_one * user_integer_two
print(f"The product of your two integers is {user_integer_product}")

check_if_same = bool(user_integer_one == user_integer_two)
print(f"It is {check_if_same} that your integers are the same.")

if user_integer_one == user_integer_two:
    print("Your integers are the same")
else:
    print("Your integers are not the same")
