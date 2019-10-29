from operator import mul
from functools import reduce

def triangle(row):
	'''
	>>> triangle(0)
	[]
	>>> triangle(1)
	[[1]]
	>>> triangle(2)
	[[1], [1, 1]]
	>>> triangle(3)
	[[1], [1, 1], [1, 2, 1]]
	>>> triangle(4)
	[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
	>>> triangle(5)
	[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
	>>> triangle(-1)
	Traceback (most recent call last):
	AssertionError: invalid number of rows
	>>> triangle(3.14)
	Traceback (most recent call last):
	AssertionError: invalid number of rows
	'''
	triangle_seq = []
	assert (isinstance(row, int) and row >= 0), "invalid number of rows"
	
	if row == 0: 
		return triangle_seq
	else:
		triangle_seq = [[1]]
		for _ in range(1,row):
			triangle_seq.append([1]+ [sum(pair) for pair in zip(triangle_seq[-1], triangle_seq[-1][1:])]+[1])
			#triangle_seq.append(nest)
	return triangle_seq


def hexagon(row, col):
	'''
	>>> hexagon(8, 4)
	[15, 20, 35, 70, 56, 21]
	>>> hexagon(16, 7)
	[2002, 3003, 6435, 11440, 8008, 3003]
	>>> hexagon(3, 3)
	Traceback (most recent call last):
	AssertionError: invalid internal position
	'''
	assert (isinstance(row, int) and isinstance(col, int) and row > 2 and 1<col<row), "invalid internal position"
	#in_row = row - 1
	in_col = col - 1 
	ts = triangle(row+1)
	return [ ts[-i][in_col + j] for i, j in ((3, -1), (3, 0), (2, 1), (1,1),(1,0),(2,-1))]
	#hex_list.append([ts[row-2][col-1]+ts[row-2][col]]+)
	
def square(row, col):
	'''
	>>> square(8, 4)
	'15 x 20 x 35 x 70 x 56 x 21 = 864360000 = 29400 x 29400'
	>>> square(16, 7)
	'2002 x 3003 x 6435 x 11440 x 8008 x 3003 = 10643228293383247161600 = 103166022960 x 103166022960'
	>>> square(3, 3)
	Traceback (most recent call last):
	AssertionError: invalid internal position
	'''
	hex_ = hexagon(row, col)
	all_mul = reduce(mul, hex_, 1)
	return "{0} = {1} = {2} x {2}".format(' x '.join(str(x) for x in hex_), all_mul, round(all_mul**0.5))



if __name__ == '__main__':
	import doctest
	doctest.testmod()