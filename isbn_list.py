def int_isbn(num_):
	'''
	>>> int_isbn('9-9715-0210-0')
	True
	>>> int_isbn('997-150-210-0')
	False
	>>> int_isbn('9-9715-0210-8')
	False
	'''
	if not isinstance(num_, str):
		return False 

	sp_lisnum = num_.split('-')
	tuple_isbn = tuple(len(i) for i in sp_lisnum)

	if tuple_isbn != (1,4,4,1):
		return False

	clean_num = ''.join(sp_lisnum)

	if not clean_num[:-1].isdigit():
		return False

	return eval_isbn(clean_num) == num_[-1]
		

def eval_isbn(num_):
	'''
	>>> eval_isbn('997150210')
	'0'
	'''
	check = sum((i+1)*int(num_[i])for i in range(9)) % 11

	return 'X' if check == 10 else str(check)    

if __name__ == '__main__':
	import doctest
	doctest.testmod()