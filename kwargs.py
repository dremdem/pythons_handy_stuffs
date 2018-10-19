def a(**k):
	b = k
	for i in k:
		if i == 'f':
			b['f'] = k['f'] + '... Yeah!!'
	return b

print(a(i=100, b="qwertyu", c=[1, 2, 3], f='Lola..'))


p = {
	'a': 'qweqwe',
	'b': 'aaaaaaaa',
	'f': 'Lola...'
}

print(a(**p))