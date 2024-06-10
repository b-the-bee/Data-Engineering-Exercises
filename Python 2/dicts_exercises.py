car1_owners = [
    "Bob",
    "Jeff"
]

car = {
    'mileage': 50000,
    'owners': car1_owners,
    'model': 'Audi',
    'valid_mot': True,
    'hand_drive': 'left'
}
# 1
car["colour"] = "Red"
print(car["colour"])

# 2
car["model"] = "Ford"
print(car["model"])

# 3
del car["model"]
print(car)

# 4
car_as_kv = list(car.items())
print(car.items())
print(car_as_kv)
for (red, green) in car_as_kv:
    print(f"key: {red}, value: {green}")
