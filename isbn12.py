'''
>>> code = ISBN13(9780136110675)
>>> print(code)
978-0-13611067-5
>>> code
ISBN13(9780136110675, 1)
>>> code.isValid()
True
>>> code.asISBN10()
'0-13611067-3'
'''

class ISBN13(object):
	"""docstring for ISBN"""
	def __init__(self, seq, country=1):
		self.seq = str(seq)
		self.country = int(country)
		assert (1 <= self.country <= 5), 'invalid ISBN code'
		
	def __str__(self):
		return '{}-{}-{}-{}'.format(self.seq[0:3], self.seq[3], self.seq[4:-1], self.seq[-1])

	def __repr__(self):
		return 'ISBN13({}, {})'.format(self.seq, self.country)

	def isValid(self):
		#if self.seq[0:3] is not '978' or '979':
		#	return False

		check = sum([3*int(i) if index_%2 else int(i) for index_,i in enumerate(self.seq[:-1])])
		return str((10-check% 10)%10)==self.seq[-1]

	def asISBN10(self):
		def checkdigit(code):
		# compute ISBN-10 check digit
			check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
		# convert the check digit into string representation
			return 'X' if check == 10 else str(check)

		code = self.seq[3:-1]
		check = checkdigit(code)
		return '{}-{}-{}'.format(
			code[:self.country],
			code[self.country:],
			check
		)
if __name__ == '__main__':
	import doctest
	doctest.testmod()