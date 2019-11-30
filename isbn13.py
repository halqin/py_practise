def  isISBN13(code):
	"""
	>>> isISBN13('9789743159664')
	True
	>>> isISBN13('9787954527409')
	False
	>>> isISBN13('8799743159665')
	False
	"""
	if not isinstance(code, str): return False
	if not code[:12].isdigit(): return False
	if len(code) != 13: return False
	# for i in range(0, 12, 2): o += int(code[i])
	# for j in range(1, 12, 2): e += int(code[j])
	def checkdigit(code):
		check = sum( (3 if i%2 else 1)  *int(code[i])for i in range(12))
		return str((10- check) % 10)
	
	return checkdigit(code) == code[-1]


if __name__ == '__main__':
	import doctest
	doctest.testmod()