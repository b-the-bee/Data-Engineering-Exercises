"""Loops exercises as part of Python 2"""

# 1

for i in range(0,11):
    print(i)
    
# 2
i = 0
while i <= 10:
    print(i)
    i += 1
    


nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

# 3 
for item in nums:
    print(item)

# 4

for i in range(0,11):
    print(i)#
else:
    print("Done!")

# 5

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            print(item1)


            
import random
while True:
    random_integer = random.randint(1, 100)
    print(random_integer)
    if random_integer % 5 == 0:
        break
    elif random_integer % 3 == 0:
        print("Skipping...")
        continue
    