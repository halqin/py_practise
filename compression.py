'''
>>> zip = ZIP('codes.txt')

>>> zip.symbol2bitstring('i')
'1000'
>>> zip.symbol2bitstring('e')
'000'
>>> zip.symbol2bitstring('T')
Traceback (most recent call last):
AssertionError: unknown symbol "T"
>>> zip.bitstring2symbol('1000')
'i'
>>> zip.bitstring2symbol('000')
'e'
>>> zip.bitstring2symbol('01')
Traceback (most recent call last):
AssertionError: invalid bitstring
>>> zip.compress('internet')
'1000001001100001100000100000110'
>>> len(zip.compress('internet'))
31
>>> zip.compress('internet explorer')
'1000001001100001100000100000110111000100101001111001001101100000011000'
>>> zip.compress('mozilla firefox')
Traceback (most recent call last):
AssertionError: unknown symbol "z"
>>> zip.decompress('1000001001100001100000100000110')
'internet'
>>> zip.decompress('1000001001100001100000100000110111000100101001111001001101100000011000')
'internet explorer'
>>> zip.decompress('10000010011000011000001000001101')
Traceback (most recent call last):
AssertionError: invalid bitstring
>>> zip.decompress('10000010011000011000000000110')
Traceback (most recent call last):
AssertionError: invalid bitstring
'''
class ZIP(object):
	"""docstring for ClassName"""
	def __init__(self, test):
		self.readdict={r.rstrip('\n')[0]:r.rstrip('\n')[2:] for r in open(test, 'r')}
		#print(self.readdict)
		

	def symbol2bitstring(self, symbol_):
		assert (self.readdict.get(symbol_)!= None), 'unknown symbol "{}"'.format(symbol_)
		return self.readdict[symbol_]


	def bitstring2symbol(self, codes):
		self.decode = {j:i for i,j in self.readdict.items()}
		assert (self.decode.get(codes)!= None), "invalid bitstring"
		return self.decode[codes]


	def compress(self, seq):
		return ''.join([self.symbol2bitstring(i) for i in seq])

	def decompress2(self, seq):
		j = 0
		i = 0
		total = 0
		result = ''
		count = 0
		while total != len(seq):
			while self.decode.get(seq[total:total+i]) == None:
				i = j%3+3
				j += 1
				count +=1
				assert (count%4 != 0), "invalid bitstring"
			result += self.decode.get(seq[total:total+i])
			total += i
			i = 0
			count = 0
		return result

	def decompress(self, seq):
		result=''
		while seq:
			prefix = 1
			while (prefix <= len(seq) and seq[:prefix] not in self.decode):
				prefix +=1
			if prefix <= len(seq):
				result +=self.decode[seq[:prefix]]
				seq = seq[prefix:]
			else:
				raise AssertionError('invalid bitstring')
		return result
				





if __name__ == '__main__':
	import doctest
	doctest.testmod()