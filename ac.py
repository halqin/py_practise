def pattern(str_):
	'''
	>>> pattern('AC Melon')
	'_C M_l_n'
	>>> pattern('slipstack')
	'sl_pst_ck'
	>>> pattern('Wander Women')
	'W_nd_r W_m_n'
	>>> candidates = bloopers('wheeloffortune.txt')
	>>> candidates['_C M_l_n']
	{'AC Melon', 'AC Milan'}
	>>> candidates['sl_pst_ck']
	{'slapstick', 'slipstack'}
	>>> candidates['W_nd_r W_m_n']
	{'Winder Woman', 'Wander Women', 'Wonder Woman'}
	'''
	vowels = list('aeiou')
	newlist = ['_' if i.lower() in vowels else i for i in str_ ]

	return ''.join(newlist)

def bloopers(text, occurrences = 1, length = 1):
	resultDict = dict()
	reader = open(text, 'r')
	for line in reader:
		ls = line.strip()
		pattern_ = pattern(ls)
		#word = resultDict.get(pattern_)
		if len(ls) >= length:
			if pattern_ in resultDict:
				resultDict[pattern_].add(ls)
			else:
				resultDict[pattern_] = {ls}

	return resultDict if occurrences == 1 else{
		key:words
		for key, words in resultDict.items()
		if len(words) >= occurrences
	}


if __name__ == '__main__':
	import doctest
	doctest.testmod()