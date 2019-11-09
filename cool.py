def serialNumber(seq):

	'''
	>>> serialNumber(834783)
	'00834783'
	>>> serialNumber('47839')
	'00047839'
	>>> serialNumber(834783244839184)
	'834783244839184'
	>>> serialNumber('4783926132432*')
	Traceback (most recent call last):
	AssertionError: invalid serial number
	'''

	assert ( 
		(isinstance(seq, str) and seq.isdigit() and int(seq) != 0 ) or 
		(isinstance(seq, int) and seq > 0) 
		), 'invalid serial number'
	 
	return str(seq).zfill(8)



def solid(seq):
	'''
	>>> solid(44444444)
	True
	>>> solid('44544444')
	False
	'''
	l = len(str(seq))
	vect = int(''.join(('1',)*l))

	return serialNumber(seq) and int(seq)%vect == 0

def radar2(seq):
	'''
	>>> radar2(44444444)
	False

	>>> radar('1822816')
	False
	'''

	if serialNumber(seq):
		for i in range(2, len(str(seq))//2+1):
			if str(seq)[:i] == str(seq)[i:i+i][::-1] and not solid(seq):
				return True 
		return False

def repeater2(seq):
	'''
	>>> repeater(20012001)
	True
	>>> repeater('83289439')
	False
	'''
	if serialNumber(seq):
		for i in range(2, len(str(seq))//2+1):
			if str(seq)[:i] == str(seq)[i:i+i] and not solid(seq):
				return True 
		return False
	return

def radar(seq):
	number = serialNumber(seq)
	half = len(number) //2
	return number[:half] == number[half:][::-1] and not solid(number)

def repeater(seq):
	number = serialNumber(seq)
	half = len(number) //2
	return number[:half] == number[half:] and not solid(number)

def radarRepeater(seq):
	'''
	>>> radarRepeater('12211221')
	True
	>>> radarRepeater('83289439')
	False
	'''
	return radar(seq) and repeater(seq)

def numismatist(seq, kind = solid):
	'''
	>>> numismatist([33333333, 1133110, '77777777', '12211221'])
	[33333333, '77777777']
	>>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
	[1133110, '12211221']
	>>> numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater)
	['12211221']
	'''
	# result = []
	# if kind==None or kind == solid:
	# 	result.extend([i for i in seq if solid(i)])
	# elif kind == radar:
	# 	result.extend([i for i in seq if radar(i)])
	# elif kind == repeater:
	# 	result.extend([i for i in seq if repeater(i)])
	# elif kind == radarRepeater:
	# 	result.extend([i for i in seq if radarRepeater(i)])


	return [ i for i in seq if kind(i)]




if __name__ == 'main':
	import doctest
	doctest.testmod()



