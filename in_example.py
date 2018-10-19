def in_test(a, b=None):
	if b in a or b is None:
		print('yaeeee')
	else:
		print('oops')

a = [1, 2, 3]


in_test(a, 1)

in_test(a, 4)

in_test(a, None)



