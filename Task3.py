BACKPACK_CAPACITY = 30

equipment = {'мясо сушеное': 5, 
            'консервы': 3, 
            'вода': 3, 
            'горелка': 1, 
            'посуда': 2, 
            'спальник': 2,
            'одежда': 15,
            'электроприборы': 5,
            'аккумуляторы': 5}


res = 0
for thing, weight in equipment.items():
    if weight <= BACKPACK_CAPACITY:
        res += weight
        print(f'{thing :<20} {weight}')
        BACKPACK_CAPACITY -= weight

print(f'Equipment weight:   {res}')