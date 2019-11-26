def clock():
	import random
	for _ in range(100):
		print('{}:{}'.format(random.randrange(0,12), random.randrange(0,60,5)))


clock()