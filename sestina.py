def endword(str_):
	'''
	>>> endword("Lo ferm voler qu'el cor m'intra")
	'intra'
	>>> endword("no'm pot ges becs escoissendre ni ongla")
	'ongla'
	>>> endword("de lauzengier qui pert per mal dir s''arma??") == 'arma'
	True
	>>> stanzas('sestina0.txt')
	[['intra', 'ongla', 'arma', 'verja', 'oncle', 'cambra'], ['cambra', 'intra', 'oncle', 'ongla', 'verja', 'arma'], ['arma', 'cambra', 'verja', 'intra', 'ongla', 'oncle'], ['oncle', 'arma', 'ongla', 'cambra', 'intra', 'verja'], ['verja', 'oncle', 'intra', 'arma', 'cambra', 'ongla'], ['ongla', 'verja', 'cambra', 'oncle', 'arma', 'intra'], ['oncle', 'arma', 'intra']]
	>>> stanzas('sestina1.txt')
	[['enters', 'nail', 'soul', 'rod', 'uncle', 'room'], ['room', 'enters', 'uncle', 'nail', 'rod', 'soul'], ['soul', 'room', 'rod', 'enters', 'nail', 'uncle'], ['uncle', 'soul', 'nail', 'room', 'enters', 'rod'], ['rod', 'uncle', 'enters', 'soul', 'room', 'nail'], ['nail', 'rod', 'room', 'uncle', 'soul', 'enters'], ['nail', 'soul', 'enters']]
	>>> stanzas('sestina2.txt')
	[['woe', 'sound', 'cryes', 'part', 'sleepe', 'augment'], ['augment', 'woe', 'sound', 'cryes', 'part', 'sleepe'], ['sleepe', 'augment', 'woe', 'sound', 'cryes', 'part'], ['part', 'sleepe', 'augment', 'woe', 'sound', 'cryes'], ['cryes', 'part', 'sleepe', 'augment', 'woe', 'sound'], ['sound', 'cryes', 'part', 'sleepe', 'augment', 'woe'], ['sound', 'part', 'augment']]
	>>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'])
	['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
	>>> permutation(['woe', 'rose', 'rhyme', 'love', 'sang', 'heart'])
	['heart', 'woe', 'sang', 'rose', 'love', 'rhyme']
	>>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme'])
	['rhyme', 'rose', 'sang', 'love', 'heart']
	>>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 2, 4, 3])
	['woe', 'rose', 'rhyme', 'love', 'sang', 'heart']
	>>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 5, 4, 3, 2, 1])
	['woe', 'rhyme', 'sang', 'heart', 'love', 'rose']
	>>> permutation(['rose', 'love', 'heart', 'sang', 'rhyme', 'woe'], [6, 1, 5, 3, 4, 3])
	Traceback (most recent call last):
	AssertionError: invalid permutation
	>>> sestina('sestina0.txt')
	True
	>>> sestina('sestina0.txt', [6, 1, 5, 2, 4, 3])
	True
	>>> sestina('sestina1.txt')
	True
	>>> sestina('sestina2.txt')
	False
	>>> sestina('sestina2.txt', [6, 1, 2, 3, 4, 5])
	True
	'''
	stop = None
	start = -1
	s = list(str_)
	while not (''.join(s[start:stop])).isalpha():
		if stop is None:stop = 0
		stop -= 1
		start -= 1
	while ''.join(s[start:stop]).isalpha():
		start -= 1
	return ''.join(s[start+1:stop])


def stanzas(text):
	reader = open(text, 'r')
	result,nestresult = [], []
	for line in reader:
		if line.strip():
			nestresult.append(endword(line).lower())
		elif nestresult:
			result.append(nestresult)
			nestresult=[]
	result.append(nestresult)
	return result	

def permutation(seq, pattern = None):
	len_ = len(seq)
	result = []
	import math
	seq1 = seq[:math.floor(len_/2)]
	seq2 = seq[math.floor(len_/2):]

	if pattern is None:
		j = 0
		for i in seq2[::-1]:
			seq1.insert(j, i)
			j+=2
		result = seq1
	else:
		assert (
			#len(set(pattern))==len(pattern) and 
			set(i+1 for i in range(len(seq)))==set(pattern)
			), 'invalid permutation'
		for i in pattern:
			result.append(seq[i-1])
	return result

def sestina(text, pattern = None):
	stanzasList = stanzas(text)
	restult = all([permutation(stanzasList[i], pattern) == stanzasList[i+1] for i in range(len(stanzasList)-2)])
	n = len(stanzasList[0])
	if len(stanzasList) == n + 1:
	# check if the envoi has n // 2 lines
		if len(stanzasList[-1]) != n // 2:
			return False
	# check if endwords of the envoi are also endwords of the other stanzas
		if not set(stanzasList[-1]) <= set(stanzasList[0]):
			return False
	if len(stanzasList) not in {n, n + 1}:
		return False

	if not stanzasList:
		return False

	for stanza in range(1, n):
		if stanzasList[stanza] != permutation(stanzasList[stanza - 1], pattern):
			return False
	return restult and set(stanzasList[-1]).issubset(stanzasList[0])





if __name__ == '__main__':
	import doctest
	doctest.testmod()





















