#a = list()
#k = 0
#for i in range(5):
#    a.append(dict())
#    for j in ['a', 'b', 'c', 'd', 'e']:
#        k = k + 1
#        a[i][j] = 100 + k

data = [
        {'a': 101, 'b': 102, 'c': 103, 'e': 105}, 
        {'a': 106, 'b': 107, 'e': 110}, 
        {'a': 111, 'b': 112, 'd': 114, 'e': 115}, 
        {'a': 116, 'd': 119, 'e': 120}, 
        {'a': 121, 'd': 124, 'e': 125}
        ]

all_keys = set().union(*(d.keys() for d in data))

for i in range(0, len(data)):
    for key in all_keys:
        if key not in [k for k in data[i].keys()]:
            data[i][key] = ' '

print(data)            
