def isISBN(code, isbn13 = True):
	'''
	>>> isISBN('9789027439642', False)
	False
	>>> isISBN('9789027439642', True)
	True
	>>> isISBN('9789027439642')
	True
	>>> isISBN('0012345679')
	False
	>>> isISBN('080442957X', False)
	True
	'''	
	
	return isISBN13(code) if isbn13 else isISBN10(code) 

def isISBN10 (code):
	'''
	>>> isISBN10('080442957X')
	False
	'''
	if not isinstance(code, str): return False
	# tuple_list = tuple([len(i)for i in code.split('-')])
	if len(code) != 10: return False
	isbn_sum = sum((i+1)*int(code[i]) for i in range(len(code)-1))
	if isbn_sum % 11 == 10 and code[9] == 'X': 
		return True
	else:
		return str(isbn_sum % 11 ) == code[9]

	

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



def areISBN(code, isbn13=None):
	'''
	>>> codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']
	>>> areISBN(codes)
	[False, True, True, True, False, False, False, True, False]
	>>> areISBN(codes, True)
	[False, False, False, False, False, False, False, True, False]
	>>> areISBN(codes, False)
	[False, True, True, True, False, False, False, False, False]
	'''
	# code_list = code.split(',')
	result = []
	for i in code:
		if isinstance(i, str):
			if isbn13 is None:
				if len(i) == 13:
					result.append(isISBN(i, True))
				else:
					result.append(isISBN(i, False))
			else:
				result.append(isISBN(i, isbn13))
		else:		
			result.append(False)
	return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()