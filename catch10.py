def missing_parameter(dic_, str_):
	'''
	>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'B':4}, 'FDVBH')
	'V'
	>>> missing_parameter({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}, 'FDVBH')
	'F'
	>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'X':4}, 'FDVBH')
	Traceback (most recent call last):
	AssertionError: invalid parameters
	>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2}, 'FDVBH')
	Traceback (most recent call last):
	AssertionError: invalid parameters
	'''
	assert (len(dic_) == len(str_)-1), 'invalid parameters'
	keyList = list(dic_.keys())

	for i in keyList:
		assert (i in str_), 'invalid parameters'

	for i in str_:
		if dic_.get(i, None) == None:
			return i

	

def juggle(parameters):
	'''
	>>> juggle({'F':1.2, 'D':0.6, 'H':2, 'B':4})
	{'F': 1.2, 'D': 0.6, 'B': 4.0, 'V': 0.3, 'H': 2.0}
	'''
	missing = missing_parameter(parameters, 'FDVBH')

	# compute value of missing parameter
	if missing == 'B':
		H, F, D, V = (parameters[key] for key in 'HFDV')
		parameters['B'] = H * (F + D) / (V + D)
	elif missing == 'H':
		B, V, D, F = (parameters[key] for key in 'BVDF')
		parameters['H'] = B * (V + D) / (F + D)
	elif missing == 'F':
		B, V, D, H = (parameters[key] for key in 'BVDH')
		parameters['F'] = B * (V + D) / H - D
	elif missing == 'V':
		H, F, D, B = (parameters[key] for key in 'HFDB')
		parameters['V'] = H * (F + D) / B - D
	else:
		H, F, B, V = (parameters[key] for key in 'HFBV')
		parameters['D'] = (H * F - B * V) / (B - H)
	# return dictionary with floating point values for all parameterss
	return {key: float(value) for key, value in parameters.items()}

def juggler(**kwargs):
	'''
	>>> juggler(F=1.2, D=0.6, H=2, B=4)
	{'F': 1.2, 'D': 0.6, 'B': 4.0, 'V': 0.3, 'H': 2.0}
	>>> juggler(D=0.6, B=4, V=0.3, H=2)
	{'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2.0, 'B': 4.0}
	>>> juggler(F=1.2, D=0.6, H=2, X=4)
	Traceback (most recent call last):
	AssertionError: invalid parameters
	'''

	return juggle(kwargs)
	


if __name__ == '__main__':
	import doctest
	doctest.testmod()








