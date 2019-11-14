def isbn13(seq):

	"""

	Checks whether or not the given ISBN-13 code is valid.

	>>> isbn13('9789743159664')
	True

	>>> isbn13('9787954527409')
	False

	>>> isbn13('8799743159665')
	False

	"""
	index_ = [x%2 for x in range(12)]	
	e  = sum([int(x)*int(y) for x,y in zip(seq, index_)])
	#print(e)
	index_.reverse()
	o = sum([int(x)*int(y) for x,y in zip(seq, index_)])
	#print(o)
	if seq[:3] not in {'978', '979'}:
		return False
	if not isinstance(seq, str):
		return False
	if len(seq) != 13:
		return False
	if not seq[:12].isdigit():
		return False

	return seq[-1] == str((10 - (o+3*e) % 10) % 10)



		
def overview(codes):
	'''
	>>> codes = [
	...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
	...    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
	...    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
	...    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
	...    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
	...    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
	...    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
	...    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
	...    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
	...    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
	...    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
	...    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
	...    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
	...    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
	... ]
	>>> overview(codes)
	English speaking countries: 8
	French speaking countries: 4
	German speaking countries: 6
	Japan: 3
	Russian speaking countries: 7
	China: 8
	Other countries: 11
	Errors: 9
	'''

	groups = {}

	for i in range(11):
		groups[i] = 0

	for seq in codes:
		if isbn13(seq):
			groups[int(seq[3])] +=1

		else:
			groups[10] +=1
	print(groups)




	print('English speaking countries: {}'.format(groups[0] + groups[1]))

	print('French speaking countries: {}'.format(groups[2]))

	print('German speaking countries: {}'.format(groups[3]))

	print('Japan: {}'.format(groups[4]))

	print('Russian speaking countries: {}'.format(groups[5]))

	print('China: {}'.format(groups[7]))

	print('Other countries: {}'.format(groups[6] + groups[8] + groups[9]))

	print('Errors: {}'.format(groups[10]))


if __name__ == '__main__':
	import doctest
	doctest.testmod()