def coordinates(text):
	'''
	>>> coordinates('photo1.txt')=={(10, 8), (5, 5), (6, 8), (6, 6), (7, 1), (10, 7), (9, 8), (10, 10), (6, 0), (1, 4), (0, 10), (1, 10), (5, 1), (8, 6), (10, 0), (9, 6), (2, 4), (7, 2), (8, 4)}
	True
	>>> coordinates('photo2.txt')=={(10, 8), (4, 7), (6, 8), (7, 1), (10, 7), (10, 10), (9, 8), (6, 0), (0, 7), (1, 4), (7, 7), (8, 7), (1, 10), (5, 1), (10, 0), (9, 6), (2, 4), (7, 2), (8, 4)}
	True
	>>> divergence('photo1.txt', 'photo2.txt')==({(8, 6), (5, 5), (0, 10), (6, 6)}, {(4, 7), (7, 7), (0, 7), (8, 7)})
	True
	>>> planets('photo1.txt', 'photo2.txt')=={(4, 7): {(5, 5), (6, 6)}, (8, 7): {(8, 6)}, (7, 7): {(8, 6), (6, 6)}, (0, 7): {(0, 10)}}
	True
	>>> print(comparator('photo1.txt', 'photo2.txt'))
	-------n--o-
	----*-----*-
	----*-------
	------------
	-------n----
	-*---o------
	*-----o-*---
	-**----n----
	----*-on----
	------*-*---
	*------**-*-
	'''
	reader = open(text, 'r')
	rowNum = 0
	coordSet = set()
	for i in reader:
		colNum = 0
		row = i.strip()
		for j in row:
			if j == '*':
				coord = (rowNum, colNum)
				coordSet.add(coord)
			colNum += 1
		rowNum += 1
	#print(coordSet)
	return coordSet

def divergence(text1, text2):
	oneTwo =set()
	Twoone = set()
	coord1 = coordinates(text1)
	coord2 = coordinates(text2)
	for i in coord1:
		if i not in coord2:
			oneTwo.add(i)
	for j in coord2:
		if j not in coord1:
			Twoone.add(j)
	resultTuple = (oneTwo, Twoone)
	return resultTuple

def planets(old, new):
	def distance(coord1, coord2):
		x1, y1 = coord1
		x2, y2 = coord2
		return (x1- x2)**2 + (y1-y2)**2
	old,new = divergence(old,new)
	coordinates = {}
	for coord1 in new:
		nearest, stars = None, set()
		for coord2 in old:
			d = distance(coord1, coord2)
			if nearest is None or d < nearest:
				nearest = d
				stars={coord2}
			elif d==nearest:
				stars.add(coord2)
		coordinates[coord1]=stars
	return coordinates

			
def comparator(old, new):
	starmap = [list(i.rstrip()) for i in open(old,'r')]
	old, new = divergence(old, new)
	for x,y in old:
		starmap[x][y] = 'o'
	for x,y in new:
		starmap[x][y] = 'n'

	return '\n'.join([''.join(i) for i in starmap])


if __name__ == '__main__':
	import doctest
	doctest.testmod()

























