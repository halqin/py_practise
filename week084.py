'''
>>> next([32, 9, 14, 3])
(23, 5, 11, 29)
>>> next((1, 2, 1, 2, 1, 0))
(1, 1, 1, 1, 1, 1)
>>> next((1, 2, 1, 2, 1, 1))
(1, 1, 1, 1, 0, 0)
>>> ducci([32, 9, 14, 3])
((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
>>> ducci((1, 2, 1, 2, 1, 0))
((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
>>> ducci((1, 2, 1, 2, 1, 1))
((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))
>>> period([32, 9, 14, 3])
0
>>> period((1, 2, 1, 2, 1, 0))
0
>>> period((1, 2, 1, 2, 1, 1))
6
'''
def next(seq):
	return tuple(abs(seq[i]-seq[(i+1)%len(seq)]) for i in range(len(seq)))	

def ducci(seq):
	seq=tuple(seq)
	result_list = tuple()
	while sum(seq) != 0 and seq not in result_list:
		result_list += (seq,)
		seq = next(seq)
	result_list +=(seq,)
	return result_list

def period(seq):
	ducci_res=ducci(seq)
	return 0 if len(ducci_res) == len(set(ducci_res)) else len(ducci_res) - ducci_res.index(ducci_res[-1])-1



if __name__=='__main__':
	import doctest
	doctest.testmod()
