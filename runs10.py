def group2(seq):
	# same value
	# distinct color 
	'''
	>>> group2(['4R', '4B', '4Y', '4K'])
	True
	>>> group2({'6B', '7B', '8B', '9B', '10B'})
	False
	>>> group2(('11R', '2B', '7Y', '2B', '9K'))
	False
	'''
	if len(seq) > 4:
		return False

	colorDic = {}
	colorList = list('RYBK')
	for i in colorList:
		colorDic[i] = 0

	numDic ={}
	for i in range(13):
		numDic[str(i+1)] = 0

	for i in seq:
		numDic[i[0]] +=1
		colorDic[i[1]] += 1

	#print(numDic.values())
	#print(colorDic.values())

	numWithout = without_(numDic, seq[0][0])

	if sum(numWithout.values()) != 0:
		return False
	for i in colorDic.values():
		if i>=2:
			return False

	return True


def group(seq):
	'''
	>>> group(['4R', '4B', '4Y', '4K'])
	True
	>>> group({'6B', '7B', '8B', '9B', '10B'})
	False
	>>> group(('11R', '2B', '7Y', '2B', '9K'))
	False
	'''
	if not three_check(seq):
		return False

	colorSet = {x[-1] for x in seq}
	if len(colorSet) != len(seq):
		return False

	numSet = {x[:-1] for x in seq}
	if len(numSet) != 1:
		return False
	return True


			
def without_(d, keys):
	return {x:d[x] for x in d if x not in keys}

def three_check(seq):
	return (
		len(seq) >= 3 and
		len(set(seq)) == len(seq)
		)


def run(seq):
	'''
	>>> run(['4R', '4B', '4Y', '4K'])
	False
	>>> run({'6B', '7B', '8B', '9B', '10B'})
	True
	>>> run(('11R', '2B', '7Y', '2B', '9K'))
	False
	'''
	colorSet = {x[-1] for x in seq}
	#print (colorSet)
	if len(colorSet) != 1:
		return False
	if not three_check(seq):
		return  False

	numlist = sorted([int(x[:-1]) for x in seq])
	for i in range(len(numlist)-1):
		if numlist[i] + 1 != numlist[i+1]:
			return False

	return True

if __name__ == '__main__':
	import doctest
	doctest.testmod()