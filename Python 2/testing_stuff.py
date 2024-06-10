# # import sys
# # sys.set_int_max_str_digits(4399090)
# # i = 2
# # while False:
# #     print(i)
# #     i = i **  999331
    
# # for x in range(0,5):
# # 	print(f"Current number is {x}.")

# # adjectives = ["red", "big", "tasty"]
# # fruits = ["apple", "banana", "cherry"]

# # for adj in adjectives:
# #   for fruit in fruits:
# #     print(adj, fruit)

# # fruits = ["apple", "banana", "cherry"]

# # for fruit in fruits:
# #     print(fruit)
# #     if fruit == "banana":
# #         break

# # data = {
# # 		"key": "value",
# # 		"fruits": ["Apples", "Bananas", "Oranges"],
# # }

# # data["fruits"]
# # print(data[0])

# def greet(name):
#     statement = f"Hello {name}."
#     return statement

# print(greet("Sam"))

# def exponent(base):
#     exponented = base ** base
#     return exponented

# print(exponent(5))

# a = "One"
# b = "two"

# def name_combiner (a, b):
#     print(a + b)
#     return "Good Morning" + a + b

# morning_message = name_combiner(a, b)

# print(morning_message)

# def bmi(weight, height):
#     product = weight / height ** 2
#     return product

# weight = int(input("Input your weight in kg"))
# height = float(input("Input your height in metres (2dp)"))

# print(bmi(weight, height))

# def add_numbers(num1, num2 ):
#     add_number = num1+num2
#     return add_number
# #def main ():
# num1 = float(input("enter the first number:"))
# num2 = float(input("enter the first number:"))
# print(add_numbers(num1, num2 ))

# try:
#     x = 1/0
# except:
#     print("You can't do that!")

# stuff = [1, 2, 3, 4, 5, 6, 7]
# for x in stuff:
#     print(x)


# my_string = "What"
# my_int = 23
# try:
#     my_input = int(input("Please input a number"))
# except ValueError as d:
#     print(d)
# try:
#     print(my_string + my_int)
# except Exception as e:
#     print(e)
#     print("This is your exception")



# u = 100
# n = "fifty"
# try:
#     print(u+n)
# except Exception as p:
#     my_input=int(input('Find the method of creating this'))

func = "ThisIsNotAFunc"print(func())