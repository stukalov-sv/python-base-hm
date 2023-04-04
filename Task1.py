lst = [5, 6, 75, 7, 6, 8, 9, 9, 12, 12, 12]
temp = set()
res = set()

for item in lst:
    if item in temp:
        res.add(item)
    temp.add(item)

print(f'Duplicate list: {list(res)}')