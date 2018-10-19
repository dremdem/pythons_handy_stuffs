from abc import ABCMeta, abstractmethod

class A(object):
	def bla(self):
		self.blabla()


class B(A):
	def blabla(self):
		print('blabla')

b = B()
b.bla()


class C:
	__metaclass__ = ABCMeta

	@abstractmethod
	def bong(self):
		pass

# c = C()
# c.bong()

class D(C):
	def bong(self):
		print('bong')

d = D()
d.bong()
