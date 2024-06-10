# import csv

# with open("ford_escort.csv", "r") as my_csv:
#     reader_dict = csv.DictReader(my_csv)
#     for row in reader_dict:
#         print(row)
        
        
# with open("exercise.csv", mode="w") as file:
#     fieldnames = ["first-name", "last-name", "age"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow({
#         "first-name": "Joe",
#         "last-name": "Bloggs",
#         "age": 40
#     })
#     writer.writerow({
#         "first-name": "Jane",
#         "last-name": "Smith",
#         "age": 50
#     })
# file.close()

# with open("exercise.csv", mode="a") as file:
#     writer = csv.writer(file, delimiter=",")
    
#     writer.writerow(
#         ["Mike","Wazowski",40]
#         )
# file.close


import json

with open("menu_items.json", "r") as file:
    my_data = json.load(file)
    item_ids = [item["id"] for item in my_data["menu"]["items"] if item]
    print(item_ids)
    
to_dump = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}
with open("my_dump.json", "w") as f:
    json.dump(to_dump, f)