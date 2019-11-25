'''
>>> bag = Bag('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
>>> bag.content=={'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
True
>>> print(bag)
1: JKQXZ
2: BCFHMPVWY_
3: G
4: DLSU
6: NRT
8: O
9: AI
12: E
>>> bag
Bag('AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ__')
>>> bag.remove('AEERTYOXMCNB_S')
>>> print(bag)
1: BCJKMQYZ_
2: FHPVW
3: GS
4: DLU
5: NRT
7: O
8: A
9: I
10: E
'''
class Bag(object):
	"""docstring for Bag"""
	def __init__(self, seq):	
		self.seq = seq
		self.content = self.content()
		self.count = self.count()

	def content(self):
		bagDict=dict()
		for letter in self.seq:
			if bagDict.get(letter) == None:
				bagDict[letter] = 1
			else:
				bagDict[letter] +=1
		return bagDict

	def __str__(self):
		#bag = self.content
		count_ = self.count
		return '\n'.join(
			'{}: {}'.format(
				i, ''.join(sorted(count_[i])) ) for i in sorted(count_)
						)


	def count(self):
		bagDict = dict()
		for letter,num in self.content.items():
			if bagDict.get(num) == None:
				bagDict[num] = [letter]
			else:
				bagDict[num].append(letter)
		return bagDict

	def __repr__(self):
		resultlist = []
		for num, letterList in self.count.items():
			for letter in letterList:
				resultlist.extend([letter]*num)
		return "Bag('{}')".format(''.join(sorted(resultlist)))

	def remove(self, letters):

		bag, nodig = self.content, Bag(letters).content
		assert all(letter in bag and nodig[letter] <= bag[letter] for letter in nodig), "not all letters are in the bag"
		# remove given letters from the bag
		for letter in letters:
			if bag[letter] == 1:
				del bag[letter]
			else:
				bag[letter] -= 1
		#return self.content


if __name__ == '__main__':
	import doctest
	doctest.testmod()





















