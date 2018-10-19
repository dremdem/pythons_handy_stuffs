from collections import namedtuple

Stage = namedtuple('Stage', ('name', 'start_day', 'end_day'))
s = Stage('qwewqe', 123, 234)

t = ('qwewqe', 123, 234)

s1 = Stage(*t)

t2 = ['qwewqe', 123, 234]

s2 = Stage(*t2)

