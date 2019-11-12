import random

def draw2(drawn=None):
	'''
	>>> draw()
	'6S'
	>>> draw(['6H', '3C', '3D', '8C', 'AD', '9D', '7D', 'QC'])
	'4D'
	>>> draw(drawn=('3S', '8H', '8C', '2H', 'AC'))
	'XH'
	>>> draw({'4C', 'AH', 'JS', '7S', '9H', '2H', 'QC', '2S', '3H', '7C'})
	'9S'

	'''

	random.seed(a = 6)
	num_list = list('23456789XJQA')
	suit_list = list('SHCD')
	result = ''.join((random.choice(num_list),random.choice(suit_list)))

	while drawn is not None and result in drawn:
		result = ''.join((random.choice(num_list),random.choice(suit_list)))
	return result


def draw(drawn=None):

	'''
	>>> draw()
	'6S'
	>>> draw(['6H', '3C', '3D', '8C', 'AD', '9D', '7D', 'QC'])
	'4D'
	>>> draw(drawn=('3S', '8H', '8C', '2H', 'AC'))
	'XH'
	>>> draw({'4C', 'AH', 'JS', '7S', '9H', '2H', 'QC', '2S', '3H', '7C'})
	'9S'

	'''

	random.seed(a = 6)
	num_list = '23456789XJQA'
	suit_list = 'SHCD'
	result = random.choice(num_list) + random.choice(suit_list)
	while drawn is not None and result in drawn:
		result = random.choice(num_list) + random.choice(suit_list)
	return result


def arrange(rows = 5, cols = 5):
	'''
	>>> arrange(rows=3, cols=4)
	[['5D', '4D', '4C', '9S'], ['2D', '6C', '4S', 'AD'], ['QH', 'QS', '2S', '3D']]
	>>> arrange(rows=7, cols=8)
	Traceback (most recent call last):
	AssertionError: invalid grid
	'''
	assert (rows*cols <= 52), 'invalid grid'
	draw_= []
	nestRow = []
	total = []
	for i in range(0,rows):
		for j in range(0, cols):
			nestRow.append(draw(nestRow))
		total.append(nestRow)
		nestRow = []
	
	return total
	


def extend(grid):
	'''
	>>> grid = [['QH', '9S', '3C'], ['5D', '8C', '2H']]
	>>> extend(grid)
	>>> grid
	[['QH', '9S', '3C', 'JH'], ['5D', '8C', '2H', '9H'], ['XD', 'XC', '4C', '9C']]
	'''	
	assert (
		len(grid)  >=1 and
		len(grid[0]) >= 1 and
		(len(grid) + 1)* (len(grid[0])+1) <= 52
		), 'invalid grid'

	existCards = []
	#existCards.extend([i for i in grid])
	for i in grid:
		existCards.extend(i)


	for i in grid:
		new = draw(existCards)
		existCards.append(new)
		i.append(new)

	new_row = []
	for _ in range(len(grid[0])):
		new = draw(existCards)
		new_row.append(new)
		existCards.append(new)

	grid.append(new_row)

def select(grid):
	'''
	>>> grid = [['RA', 'K6', 'RV', 'H7'], ['R6', 'KX', 'KX', 'KV'], ['R8', 'R4', 'R7', 'K3']]
	>>> select(grid)
	(1, 3)
	'''
	random.seed(1)
	rowNum = len(grid)
	colNum = len(grid[0])

	row = random.randint(0, rowNum-1)
	col = random.randint(0,colNum-1)

	return row, col

	








































if __name__ == '__main__':
	import doctest
	doctest.testmod() 