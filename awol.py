
def coordinates(test):
	'''
	>>> coords = coordinates('airports.csv')
	>>> len(coords)
	9187
	>>> type(coords)
	<class 'dict'>
	>>> coords['BRU']
	(50.902222, 4.485833)
	>>> coords['CDG']
	(49.016667, 2.55)
	>>> coords['DCA']
	(38.851944, -77.037778)
	>>> coords['LAX']
	(33.9425, -118.407222)

	>>> haversine((50.902222, 4.485833), (49.016667, 2.55)) # BRU <-> CDG
	251.2480027355068
	>>> haversine((38.851944, -77.037778), (33.9425, -118.407222)) # DCA <-> LAX
	3710.8262543589817

	>>> flightplan('DCA', 'LAX', coords)
	['DCA', 'MTO', 'HLC', 'BFG', 'LAX']
	>>> flightplan('DCA', 'LAX', coords, range=2000)
	['DCA', 'DDC', 'LAX']
	>>> flightplan('DCA', 'LAX', coords, range=4000)
	['DCA', 'LAX']

	>>> flightplan('BRU', 'CDG', coords)
	['BRU', 'CDG']
	'''
	import csv

	coords = {}
	csvfile = open(test, 'r', encoding='utf-8')
	handle = csv.reader(csvfile, delimiter=',')
	for row in handle:
		coords[row[0]] = (float(row[5]), float(row[6]))
	return coords



def coordinates2(test):

	import csv

	coords = {}
	with open(test) as csvfile:
		handle = csv.reader(csvfile, delimiter=',')
		for row in handle:
			coords[row[0]] = (float(row[5]), float(row[6]))
	return coords

def haversine(coord1, coord2):
	from math import sin, cos, radians, atan2, sqrt
	r = 6371.0
	b1, l1 = (radians(c) for c in coord1)
	b2, l2 = (radians(c) for c in coord2)
# compute Haversine distance
	a = (sin((b2 - b1) / 2) ** 2 +cos(b1)*cos(b2)*sin((l2 - l1) / 2) ** 2)
	c = atan2(sqrt(a), sqrt(1 - a))

	return 2 * r * c
	
def flightplan2(des1, des2, coords, range = 1000):
	#coord1, coord2 = (coords[des1], coords[des2])
	dis = haversine(coords[des1],coords[des2])
	if dis <= range:
		return [des1, des2]
	#assert (haversine(coords[des1],coords[des2]) <= range), 'no possible route'
	pathList = [des1, des2]
	num = 0
	while dis > range and num <len(coords):
		for num, (router,coords_) in enumerate(coords.items()):
			pathList.insert(-2,router)
			if haversine(coords[pathList[-3]],coords[pathList[-2]]) <= range: 
				dis = haversine(coords[pathList[-1]],coords[pathList[-2]])
				if dis <= range:
					return pathList
			else:
				pathList.remove(router)

def flightplan(des1, des2, coords, range = 1000):

	pathList = [des1]
	while pathList[-1] != des2:
		dis, airport = None, None
		for router,coords_ in coords.items():
			if router not in pathList and haversine(coords[pathList[-1]], coords_) <= range:
				dis_in =  haversine(coords_, coords[des2])
				if  dis is None or dis_in < dis:
					dis = dis_in
					airport = router
		assert dis is not None, 'no possible route'
		pathList.append(airport)
	return pathList

if __name__ == '__main__':
	import doctest
	doctest.testmod()
























