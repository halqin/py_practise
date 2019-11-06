def hit(hit, occupied = []):
	'''
	>>> hit(2)
	(0, [2])
	>>> hit(0, [1, 3])
	(0, [1, 3])
	>>> hit(1, (1, 3))
	(1, [1, 2])
	>>> hit(2, occupied=[1, 3])
	(1, [2, 3])
	>>> hit(3, occupied=(1, 3))
	(2, [3])
	>>> hit(4, occupied=[1, 3])
	(3, [])
	>>> hit(4)
	(1, [])
	'''
	# every hitting, one person will be added in the base, n-base means how many 1/4 did they go, i.e. 2base means 2*(1/4) have gone 
	# be careful, non zero base means adding one player in the court 
	
	result_list = []
	total_score = 0 
	corrdi_list = []

	occupied = list(occupied)

	if hit == 0:
		return tuple([0, occupied])
	if hit > 4:
		return False

	
	occupied.insert(0, 0)

	for i in occupied:
		s, corrdi_ = score(hit, i)
		total_score += s
		corrdi_list += corrdi_
	result_list = [total_score, corrdi_list]

	return tuple([total_score, corrdi_list])


def hit2(base, occupied= None):
	if occupied == None:
		occupied = []

	new_occu = [pre_occu + base for pre_occu in occupied]

	if base:
		new_occu.append(base)

	score = len([base for base in new_occu if base >=4])

	final_occu = sorted([base for base in new_occu if base <4])

	return score, final_occu







def score(hit, corrdi = 0):
	score = 0
	corrdi_ = []	
	corrdi += hit
	if corrdi >= 4:
		score = 1
	else:
		corrdi_.append(corrdi)
	return score, corrdi_

def inning(seq):

	'''
	>>> inning([0, 1, 2, 3, 4])
	(4, [])
	>>> inning((4, 3, 2, 1, 0))
	(2, [1, 3])
	>>> inning([1, 1, 2, 1, 0, 0, 1, 3, 0])
	(5, [3])
	'''
	total_score = 0
	corrdi_ = []
	for num_hit in seq: 
		hit_tuple = hit2(num_hit, corrdi_)
		score = hit_tuple[0]
		corrdi_ = hit_tuple[1]
		total_score += score
	result_list = [total_score, corrdi_]

	return tuple(result_list)


if __name__ == '__main__':
	import doctest
	doctest.testmod()