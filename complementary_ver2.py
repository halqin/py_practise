def increasing(list_):
# return boolean
	'''

	>>> increasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
	True

	'''
	for i in range(len(list_)-1):
		if  list_[i]  > list_[i+1]:
			return False
	return True




def frequencySequence(list_):
	'''
	>>> frequencySequence([2, 3, 5, 7, 11, 13])
	[0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
	>>> frequencySequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
	[2, 3, 5, 7, 11, 13, 14]
	>>> frequencySequence([5, 3, 2, 7, 8, 1, 9])
	Traceback (most recent call last):
	AssertionError: given sequence is not increasing
	'''

# return list
# ver2, dont use max function 
	assert increasing(list_), 'given sequence is not increasing'
	freqSeq, count, value = [], 0, 0 
	for i in list_:
		while value < i:
			freqSeq.append(count)
			value += 1
		count += 1

	freq.append(count)
	return freqSeq	
			


def lift(list_):
# return list
	'''
	>>> lift([2, 3, 5, 7, 11, 13])
	[3, 5, 8, 11, 16, 19]
	>>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
	[1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
	>>> lift([5, 3, 2, 7, 8, 1, 9])
	[6, 5, 5, 11, 13, 7, 16]
	'''
	add_list = []
	lift_list = []
	for i in range(1, len(list_)+1, 1):
		add_list.append(i)
	#print (add_list)
	lift_list = [x + y for x, y in zip(add_list, list_)]
	return lift_list



def complementarySequences(list_):
# return tuple ([],[])
	'''
	>>> complementarySequences([2, 3, 5, 7, 11, 13])
	([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
	>>> complementarySequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
	([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
	>>> complementarySequences([5, 3, 2, 7, 8, 1, 9])
	Traceback (most recent call last):
	AssertionError: given sequence is not increasing
	'''
	assert increasing(list_), 'given sequence is not increasing'

	l1 = lift(list_)
	l2 = lift(frequencySequence(list_))
	tp = (l1, l2)
	return tp

if __name__ == "__main__":
	import doctest
	doctest.testmod()