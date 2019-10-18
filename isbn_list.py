def int_isbn(num_):
	if not isinstance(num_, str):
		return False 

	sp_lisnum = num_.split('-')
	tup_isbn = tuple(len(i) for i in sp_lisnum)
	if tuple != (1,4,4,1):
		return False

	int_num = int(num_.replace('-',''))

	eval_isbn(int_num)
		

def eval_isbn(num_):
	    
