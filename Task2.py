def hash_check(item: object) -> bool:
    
    try:
        hash(item)
        return True
    except Exception as e:
        return False

def get_dictionary(**kwargs) -> dict:
    res = {}
    for key, value in kwargs.items():
        if hash_check(value):
            res[value] = key
        else:
            res[str(value)] = key
    return res
 
my_dict = get_dictionary(a='ffff', b=7, c=(1, 2, 3), d=[4, 5, 6])
print(my_dict)