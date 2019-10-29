def next (seq):
	'''
	>>> next([32, 9, 14, 3])
	(23, 5, 11, 29)
	>>> next((1, 2, 1, 2, 1, 0))
	(1, 1, 1, 1, 1, 1)
	>>> next((1, 2, 1, 2, 1, 1))
	(1, 1, 1, 1, 0, 0)
	'''
	next_seq = []
	n = len(seq)
	for i in range(len(seq)):
		next_seq.append(abs(seq[i]-seq[(i+1)%n]))
	return tuple(next_seq)


def ducci(seq):
	'''
	>>> ducci([32, 9, 14, 3])
	((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
	>>> ducci((1, 2, 1, 2, 1, 0))
	((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
	>>> ducci((1, 2, 1, 2, 1, 1))
	((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
	'''
	#len_seq = len(seq)
	new_tuple = []
	next1 = tuple(seq)
	#new_tuple.append(next1)
	while sum(next1) != 0 and next1 not in new_tuple:
		new_tuple.append(next1)
		next1 = next(next1)
	new_tuple.append(next1)
	return tuple(new_tuple)

def period(seq):
	'''
	>>> period([32, 9, 14, 3])
	0
	>>> period((1, 2, 1, 2, 1, 0))
	0
	>>> period([1, 5, 7, 9, 9])
	15
	'''
	ducci_seq= ducci(seq)
	index_ = ducci_seq.index(ducci_seq[-1])
	return len(ducci_seq)-1-index_



if __name__ == '__main__':
	import doctest
	doctest.testmod()






