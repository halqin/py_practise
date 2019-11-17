def fill(seq):
	'''
	>>> bag = fill('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
	>>> bag == {'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
	True
	>>> description(bag) =={1: {'Q', 'Z', 'X', 'K', 'J'}, 2: {'F', '_', 'P', 'C', 'M', 'W', 'Y', 'B', 'V', 'H'}, 3: {'G'}, 4: {'U', 'D', 'L', 'S'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'I', 'A'}, 12: {'E'}}
	True
	>>> remove('AEERTYOXMCNB_S', bag)
	>>> description(bag) == {1: {'J', '_', 'C', 'K', 'M', 'Z', 'Y', 'B', 'Q'}, 2: {'W', 'P', 'V', 'F', 'H'}, 3: {'S', 'G'}, 4: {'U', 'D', 'L'}, 5: {'N', 'R', 'T'}, 7: {'O'}, 8: {'A'}, 9: {'I'}, 10: {'E'}}
	True
	>>> remove('XXX', bag)
	Traceback (most recent call last):
	AssertionError: not all letters are in the bag
	'''
	bag = dict()
	for i in seq:
		bag[i] = bag.get(i, 0) + 1
	return bag


def description2(bag):
	bagDescri = dict()
	
	for key in bag:
		numkey = bag.get(key)
		wordset = bagDescri.get(numkey)
		if wordset == None: wordset = set()
		wordset.add(key)
		bagDescri[numkey]= wordset
	return bagDescri

def description(bag):
	bagDescri = {}
	for key,value in bag.items():
		if value in bagDescri:
			bagDescri[value].add(key)
		else:
			bagDescri[value] = {key}
	return bagDescri


def remove2(seq, bag):
	for i in seq:
		value = bag.get(i)
		assert (value is not None), 'not all letters are in the bag'
		value -= 1
		bag.update({i:value})
		if value == 0:
			del bag[i]
	#return bag
def remove(seq, bag):
	nested = fill(seq)
	assert all(
		key in bag and value <= bag[key]
		for key, value in nested.items()	
		), 'not all letters are in the bag'
	for i in seq:
		if bag[i] == 1:
			del bag[i]
		else:
			bag[i] -= 1



if __name__ == '__main__':
	import doctest
	doctest.testmod()