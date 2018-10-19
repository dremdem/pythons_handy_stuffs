import itertools

data = ['a', 'b.c', 'b.d']

sorted_data = sorted(data)

b = {
'a': 'Joe',
'c': 'sdasd',
'b': 'asdasd',
}




iterator = itertools.groupby(sorted_data, key=lambda x: x.split(".")[0])



for k, v in iterator:
	print (f'Group: {k}')
	print(list(v))
	for i in v:
		print(f'Value : {i}')

data = ['a', 'b', 'c', 'd']

iterator = itertools.groupby(sorted(data), key=lambda x: x.split(".")[0])

for k, v in iterator:
	joined_child = '.'.join(v)
	print('joined_child: %s' % joined_child)
	subkeys = joined_child[joined_child.find('.')+1:]
	print('subkeys: %s, find: %d' % (subkeys, joined_child.find('.') ))
	print(k)
	print(list(v))