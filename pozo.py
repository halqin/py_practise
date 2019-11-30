def crossSection(row, str_):
	'''
	>>> crossSection(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
	[['NS', 'SW', 'NS', 'SW', 'NW', 'NW', 'EW', 'SW'], ['NS', 'SE', 'EW', 'SW', 'EW', 'SE', 'NS', 'SW'], ['NE', 'NW', 'NS', 'NE', 'EW', 'EW', 'SW', 'SE'], ['NW', 'NE', 'SE', 'EW', 'NW', 'NW', 'SE', 'SW']]
	>>> crossSection(4, 'NSSWNSSWNWNWEWSWNSS')
	Traceback (most recent call last):
	AssertionError: invalid cross section
	'''	
	assert (len(str_)%(row*2)== 0), "invalid cross section"
	map = []
	new_map = []
	for i in range(0,len(str_),2):
		map.append(str_[i:i+2])
	#print(len(map))
	col = int(len(map)/row)
	for j in range(0, len(map), col):
		new_map.append(map[j:j+col])
	#	print(j)
	return new_map

def depth(cave):
	#if 1<= row <=2  and 1<=col<=6:
	wList = []
	eList = []
	nList = []
	sList = []
	#or x in ['W', 'E', 'N', 'S' don]:
		if x == 'W':
			neighourList = ['EW','ES', 'EN']
		elif x == 'E':			
			neighourList  = []
		elif x == 'N':
			neighourList = []
		elif x == 'S':
			neighourList = []
		else:
			print('wrong direction')


if __name__ == "__main__":
	import doctest
	doctest.testmod()