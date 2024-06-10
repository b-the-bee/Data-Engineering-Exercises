car1_owners = [
    {'sex': 'f', 'age': 30},
    {'sex': 'm', 'age': 25}
]
 
car1 = {
    'mileage': 50000,
    'owners': car_owners,
    'model': 'Audi',
    'valid_mot': True,
    'hand_drive': 'left'
}
 
car1.get('milage')
car1['mileage']
 
 
car2 = {
    'mileage': 0,
    'owners': [], # or None?
    'model': 'Ferrari',
    'valid_mot': False,
    'hand_drive': 'right'
}
 
cars = [car1, car2]

cars_dict = {
    '123456': {
        'mileage': 0,
        'owners': [], # or None?
        'model': 'Ferrari',
        'valid_mot': False,
        'hand_drive': 'right',
        'reg': '123456'
    },
    '8989456': {
        'mileage': 50000,
        'owners': car1_owners,
        'model': 'Audi',
        'valid_mot': True,
        'hand_drive': 'left',
        'reg': '8989456'
    }
}