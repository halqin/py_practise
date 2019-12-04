'''
>>> rock = Block(5, 2, 3)
>>> rock
Block(length=5, height=2, width=3, position=(0, 0))
>>> rock.area()
62.0
>>> rock.volume()
30.0
>>> rock.diagonal()
6.164414002968976
>>> rock2 = rock.slide('R')
>>> rock2
Block(length=5, height=2, width=3, position=(0, 5))
>>> rock is rock2
True
>>> rock.slide('F')
Block(length=5, height=2, width=3, position=(3, 5))
>>> rock.tilt('L')
Block(length=2, height=5, width=3, position=(3, 3))
>>> rock.tilt('B')
Block(length=2, height=3, width=5, position=(0, 3))
>>> rock.tilt('B').slide('L').tilt('L').slide('B')
Block(length=5, height=2, width=3, position=(-8, -4))
>>> rock.sail('SB')
Block(length=5, height=2, width=3, position=(-11, -4))
>>> rock.sail('TR')
Block(length=2, height=5, width=3, position=(-11, 1))
>>> rock.sail('SFSFTLSLTBTBSRSFTRTFTRTRSBSF')
Block(length=2, height=3, width=5, position=(-2, 6))

>>> rock.tilt('X')
Traceback (most recent call last):
AssertionError: invalid direction
>>> rock.sail('XY')
Traceback (most recent call last):
AssertionError: invalid movement
>>> rock.sail('TY')
Traceback (most recent call last):
AssertionError: invalid direction


>>> rock07 = Block(length=5, height=2, width=3)
>>> rock07.tilt('F')
Block(length=5, height=3, width=2, position=(2, 0))
'''

import math


class Block(object):
	def __init__(self, length, height, width,position=(0,0)):
		self.len = length
		self.hei = height
		self.wid = width
		self.x = position[0]
		self.y = position[1]

	def area(self):
		return float(2*(self.len*self.wid+self.len*self.hei+self.hei*self.wid))

	def volume(self):
		return float(self.len*self.hei*self.wid)

	def diagonal(self):
		return math.sqrt(self.len**2 + self.hei**2+self.wid**2)

	def __repr__(self):
		return '{}(length={}, height={}, width={}, position={})'.format(self.__class__.__name__, self.len, self.hei, self.wid, (self.x, self.y))

	def slide(self, direction):
		#contorl = {'f':1, 'b':-1, 'l':-1, 'r':1}
		if direction== 'F':
			self.x += self.wid
		elif direction == 'B':
			self.x -= self.wid
		elif direction == 'L':
			self.y -= self.len
		elif direction == 'R':
			self.y += self.len
		else:
			raise AssertionError('invalid direction')
		return self
		# self.__class__

	def tilt(self, direction):
		if direction in 'LR':
			self.y += self.len if direction == 'R' else -self.hei
			self.len, self.hei = self.hei, self.len
		elif direction in 'FB':
			self.x -= self.wid if direction == 'B' else -self.hei
			self.wid, self.hei = self.hei, self.wid
		else:
			raise AssertionError('invalid direction')
		return self

	def sail(self, direction):
		for i in range(0, len(direction),2):
			if direction[i:i+2][0] == 'S':
				self.slide(direction[i:i+2][1])
			elif direction[i:i+2][0] == 'T':
				self.tilt(direction[i:i+2][1])
			else:
				raise AssertionError('invalid movement')
		return self


if __name__=="__main__":
	import doctest
	doctest.testmod()