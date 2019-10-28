def merge(seq1, seq2):
	'''
	>>> merge(('A', 'B', 'C'),  [1, 2, 3])
	['A', 1, 'B', 2, 'C', 3]
	>>> merge(['A'], [1, 2, 3, 4])
	['A', 1]
	>>> merge(('A', 'B'),  (1, 2, 3, 4))
	['A', 1, 'B', 2]
	>>> merge(('A', 'B', 'C'),  [1, 2])
	['A', 1, 'B', 2]
	'''
	new_list = []
	seq1 = list(seq1)
	seq2 = list(seq2)
	zip_list = list(zip(seq1, seq2))
	for i in zip_list:
		new_list.extend(i)
	return new_list

def weave(seq1, seq2):
	'''
	>>> weave(('A', 'B', 'C'),  [1, 2, 3])
	['A', 1, 'B', 2, 'C', 3]
	>>> weave(['A'], [1, 2, 3, 4])
	['A', 1, 'A', 2, 'A', 3, 'A', 4]
	>>> weave(('A', 'B'),  (1, 2, 3, 4))
	['A', 1, 'B', 2, 'A', 3, 'B', 4]
	>>> weave(('A', 'B', 'C'),  [1, 2])
	['A', 1, 'B', 2, 'C', 1]
	'''
	seq2 = list(seq2)
	seq1 = list(seq1)
	len1 = len(seq1)
	len2 = len(seq2)
	new_list = []
	# min_len = max(len(seq2), len(seq1))
	if len2 < len1:
		while len(seq2) < len(seq1):
			seq2.extend(seq2)
	elif len1 < len2: 
		while  len(seq1) < len(seq2):
			seq1.extend(seq1)
	zip_list = list(zip(seq1,seq2))
	for i in zip_list:
		new_list.extend(i)

	#print(new_list)
	return new_list

def zipper(seq1, seq2):
	'''
	>>> zipper(('A', 'B', 'C'),  [1, 2, 3])
	['A', 1, 'B', 2, 'C', 3]
	>>> zipper(['A'], [1, 2, 3, 4])
	['A', 1, 2, 3, 4]
	>>> zipper(('A', 'B'),  (1, 2, 3, 4))
	['A', 1, 'B', 2, 3, 4]
	>>> zipper(('A', 'B', 'C'),  [1, 2])
	['A', 1, 'B', 2, 'C']
	'''	
	seq2 = list(seq2)
	seq1 = list(seq1)
	new_list = []
	len1 = len(seq1)
	len2 = len(seq2)
	zip_list = list(zip(seq1, seq2))
	for i in zip_list:
		new_list.extend(i)
	if len1 > len2:
		new_list.extend(seq1[len2:])
	else:
		new_list.extend(seq2[len1:])
	return new_list


if __name__ == "__main__":
	import doctest
	doctest.testmod()