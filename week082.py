'''
>>> increasing([2, 3, 5, 7, 11, 13])
True
>>> increasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
True
>>> increasing([5, 3, 2, 7, 8, 1, 9])
False
>>> frequencySequence([2, 3, 5, 7, 11, 13])
[0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
>>> frequencySequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
[2, 3, 5, 7, 11, 13, 14]
>>> frequencySequence([5, 3, 2, 7, 8, 1, 9])
Traceback (most recent call last):
AssertionError: given sequence is not increasing
>>> lift([2, 3, 5, 7, 11, 13])
[3, 5, 8, 11, 16, 19]
>>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
[1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
>>> lift([5, 3, 2, 7, 8, 1, 9])
[6, 5, 5, 11, 13, 7, 16]
>>> complementarySequences([2, 3, 5, 7, 11, 13])
([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
>>> complementarySequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
>>> complementarySequences([5, 3, 2, 7, 8, 1, 9])
Traceback (most recent call last):
AssertionError: given sequence is not increasing
'''


def increasing(seq):
	for i in range(len(seq[:-1])):
		if seq[i] > seq[i+1]:
			return False
	return True


def	frequencySequence(seq):
	assert (increasing(seq)), "given sequence is not increasing"
	resultList =[]
	count = 0
	for i in range(seq[-1]+1):
		for j in seq:
			if j < i+1:
				count +=1
		resultList.append(count)
		count = 0
	return resultList


def lift(seq):
	return [conut+ele+1 for conut, ele in enumerate(seq)]


def complementarySequences(seq):
	return lift(seq), lift(frequencySequence(seq))

if __name__=="__main__":
	import doctest
	doctest.testmod()