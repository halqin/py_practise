'''
>>> machine1 = T52(3, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

>>> machine1.encodeSymbol('G')
'X'
>>> machine1.encodeSymbol('S')
'H'
>>> machine1.encodeSymbol('-')
'-'

>>> machine1.decodeSymbol('X')
'G'
>>> machine1.decodeSymbol('H')
'S'
>>> machine1.decodeSymbol('-')
'-'
>>> machine1.encode('G-SCHREIBER')
'X-HLAERDIRE'
>>> machine1.decode('X-HLAERDIRE')
'G-SCHREIBER'
>>> machine2 = T52(17, 11, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
>>> machine2.encode('X-HLAERDIRE')
'M-AQLBOKROB'

>>> machine2 = T52(17, 11, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
>>> machine2.encode('X-HLAERDIRE')
'M-AQLBOKROB'

>>> machine12 = machine1 + machine2
>>> machine12.encode('G-SCHREIBER')
'M-AQLBOKROB'
>>> T52(4, 5, 'ABCDEFGHIJKLMMLKJIHGFEDCBA')
Traceback (most recent call last):
AssertionError: alphabet has repeated symbols
>>> T52(4, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Traceback (most recent call last):
AssertionError: 4 and 26 are not coprime
>>> machine1 + T52(17, 11, 'abcdefghijklmnopqrstuvwxyz')
Traceback (most recent call last):
AssertionError: alphabets are different
'''

class T52(object):
	"""docstring for T52"""
	def __init__(self, a, b, mstr):
		from math import gcd as bltin_gcd
		super(T52, self).__init__()
		self.a = int(a)
		self.b = int(b) 
		self.mstr = mstr
		self.m = len(mstr)
		assert (len(set(mstr))==self.m), "alphabet has repeated symbols"
		assert (bltin_gcd(a, self.m)==1), "{} and {} are not coprime".format(self.a, self.m)

	def encodeSymbol(self, sym):
		x = self.mstr.find(sym)
		if x!=-1:
			pos1 = (self.a*x+self.b) % self.m
			return self.mstr[pos1]
		else:
			return sym

	def decodeSymbol(self, sym):
		x = self.mstr.find(sym)
		def inv():
			for a_ in range(self.m):
				if a_*self.a%self.m == 1:
					return a_
		if x!=-1:
			pos1 = inv()*(x-self.b) % self.m
			return self.mstr[pos1]
		else:
			return sym
	def encode(self, sym):
		return ''.join([self.encodeSymbol(i) for i in sym])

	def decode(self, sym):
		return ''.join([self.decodeSymbol(i) for i in sym])

	def __add__(self, para2):
		#enx = encode(self.mstr)
		#super(T52, self).__init__()
		a=self.a*para2.a
		b=self.b*para2.a+para2.b
		assert (self.mstr==para2.mstr), "alphabets are different"
		return T52(a, b, self.mstr)






if __name__ == '__main__':
	import doctest
	doctest.testmod()





