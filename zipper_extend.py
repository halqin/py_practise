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
	new_seq = []
	for x, y in zip(seq1, seq2):
		new_seq.extend((x,y))
	return new_seq

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
	long_seq = max(len(seq1), len(seq2))
	new_seq = []
	for i in range(long_seq):
		new_seq.extend((seq1[i % len(seq1)], seq2[i % len(seq2)]))
	return new_seq

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
	new_seq = []
	len1 = len(seq1)
	len2 = len(seq2)
	for x,y in zip(seq1, seq2):
		new_seq.extend((x, y))
	if len1 < len2:
		new_seq.extend(seq2[len1:])
	else:
		new_seq.extend(seq1[len2:])
	return new_seq

if __name__ == "__main__":
	import doctest
	doctest.testmod()