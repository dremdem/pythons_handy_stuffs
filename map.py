l = [
{'a': 1, 'b': 1, 'c': 1},
{'a': 1, 'b': 1, 'c': 2},
{'a': 1, 'b': 2, 'c': 1},
{'a': 2, 'b': 1, 'c': 1}, 
]

print(sorted(l, key=lambda x: (x['a'], x['b'], x['c'])))
print(sorted(l, key=lambda x: (x['b'], x['c'])))


fruits = ['banana', 'apple', 'lemon']

print(list(map(lambda x: 'I like ' + x, fruits)))

workers = [
{'name': 'John', 'no': 5},
{'name': 'Smith', 'no': 3},
{'name': 'Geoff', 'no': 4},
{'name': 'Kirk', 'no': 1},
{'name': 'John', 'no': 2},
]

print(list(filter(lambda x: x['no']>2, workers)))


complex_list = [
{'a': 111},
{'a': 111},
{'a': 111},
{'a': 111}
]

print(list(map(lambda x: del()))
