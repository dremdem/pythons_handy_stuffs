l = [
{'a': 1, 'b': 1, 'c': 1},
{'a': 1, 'b': 1, 'c': 2},
{'a': 1, 'b': 2, 'c': 1},
{'a': 2, 'b': 1, 'c': 1}, 
]

print(sorted(l, key=lambda x: (x['a'], x['b'], x['c'])))
print(sorted(l, key=lambda x: (x['b'], x['c'])))

