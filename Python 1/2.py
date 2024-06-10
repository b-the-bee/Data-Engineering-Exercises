# """Day 2 Python"""
# # var_1 = "Beans"
# # var_2 = "On"
# # var_3 = "Toast"

# # my_string = f"{var_1} {var_2} {var_3}."

# # print(my_string)

# # big_string = f"""{my_string}
# # woah this string goes on multiple lines!
# # So it does!"""
# # print(big_string)

# # cool_list = ["Bob", "People", 3, 2, [1, 2, 3], "Bananas"]

# # print(cool_list[0])
# # print(cool_list[2:])
# # print(cool_list[:3])
# # print(cool_list[4][1])
# # print(cool_list[3:])
# # print(len(cool_list))

# # user_name = input("What is your name?\n")
# # print(f"Hello {user_name}")

# # user_num = int(input("Enter a number: "))

# # print(f"The square value of this value is {user_num * user_num}")

# # Create a variable which will store your first name. Print out the variable.
# # Create a second variable which will store your last name.
# # Concatenate the two variables and print out the result.
# # Extend the above to print the following using an f-string:
# # Hi, my name is {first_name} {last_name}.

# first_name = "Sam"
# last_name = "Brunkard"

# print(f"Hi my name is {first_name} {last_name}.")


# # Create two variables that store integer values. Calculate the product (the number you get by multiplying two or more other numbers together) of the two integers and store it in a third variable. Print the value of this variable.
# # Extend the above to print out the following: The product of {x} and {y} is {product}, replacing x, y, product with the values for the above.


# first_integer = 23
# second_integer = 32
# product_of_two = first_integer * second_integer

# # Extend the above to print out the following: The product of {x} and {y} is {product}, replacing x, y, product with the values for the above.

# print(f"The product of {first_integer} and {second_integer} is {product_of_two}.")


# # For this section, we will be operating on the below list of names.
# # Please copy this line and paste it into your code file. Remember that list indexes start at zero!

# # people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# # Retrieve the third element (the second-indexed element) and store it in its own variable.
# # Print the variable.
# # Retrieve the element third from the back of the list and store it in its own variable.
# # Print the variable.
# # Split the list into a new list with just the names Mark, Lisa, Joe and Barry.
# # Print whether or not the first and last element in the list are equal to one another.

# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
# print(people[2])
# print(people[-2])
# new_people = people[2:6]
# print(people[0] == people[-1])


# # Hint: You can use input() as many times as you like. For instance,
# # you can ask for someone's first name on one line, and their last name on another line.

# # Accept input from the user for their name. Print their name out.
# # Accept two integer inputs from the user and calculate the product. Print out the product.
# # Accept two integer inputs from the user. Use the comparison operator to print out 
# # if the two values are equal (True), or if they're not (False).

# user_name = input("What is your name please")
# print(f"Your name is {user_name}.")
# user_integer_one = int(input("What is your first integer?"))
# user_integer_two = int(input("What is your second integer?"))
# user_integer_product = user_integer_one * user_integer_two
# print(f"The product of your two integers is {user_integer_product}")

# check_if_same = bool(user_integer_one == user_integer_two)
# print(f"It is {check_if_same} that your integers are the same.")


a = 9 + 10
b = a + 2
if a == 21:
    print("21")
    if b == a:
        print("a and b are the same")
elif b == 21:
        print("b is 21 though")
else:
    print("9 + 10 doesn't equal 21")

a = 10
b = 20

if a < 10:
    print("")