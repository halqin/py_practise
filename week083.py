'''
>>> merge(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> merge(['A'], [1, 2, 3, 4])
['A', 1]
>>> merge(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2]
>>> merge(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2]
>>> weave(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> weave(['A'], [1, 2, 3, 4])
['A', 1, 'A', 2, 'A', 3, 'A', 4]
>>> weave(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2, 'A', 3, 'B', 4]
>>> weave(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2, 'C', 1]
>>> zipper(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> zipper(['A'], [1, 2, 3, 4])
['A', 1, 2, 3, 4]
>>> zipper(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2, 3, 4]
>>> zipper(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2, 'C']
'''


def merge(seq1_, seq2_):
	result = []
	for a,b in zip(seq1_, seq2_):
		result.extend([a,b])
	return result


def weave(seq1, seq2):
	newList = []
	for i in range(max(len(seq1), len(seq2))):
		newList.extend((seq1[i%len(seq1)], seq2[i%len(seq2)]))
	return newList


def zipper2(seq1, seq2):
	newList=[]
	long_L= seq1 if len(seq1)>len(seq2) else seq2
	short_L= seq1 if len(seq1)<=len(seq2) else seq2
	for i in range(len(short_L)):
		newList.extend((seq1[i%len(short_L)], seq2[i%len(short_L)]))
	newList.extend(long_L[len(short_L):])
	return newList

def zipper(seq1, seq2):
	long_L= seq1 if len(seq1)>len(seq2) else seq2
	short_L= seq1 if len(seq1)<=len(seq2) else seq2
	newList=merge(seq1, seq2)
	newList.extend(long_L[len(short_L):])
	return newList

if __name__ == '__main__':
	import doctest
	doctest.testmod()

