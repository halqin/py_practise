from unittest.mock import MagicMock
import unittest


class add_mul(object):
	"""docstring for add_mul"""
	def __init__(self, a, b, c):
		self.c = c
		self.a = a
		self.b = b

	def f1(self):
		self.mul(self.b, self.a)
		return self.c+self.mul(self.a, self.b)

	def mul(self, a, b):
		"""docstring for add"""
		return a*b


class TestAddul(unittest.TestCase):
	"""docstring for TestAddul"""
	def test_add_mul(self):
		cal_mul = MagicMock()
		# cal = add_mul(5, 100, 4)
		cal_mul.mul.return_value=15
		cal = add_mul(cal_mul)
		self.assertEqual(cal.f1(), 19)
		# cal.mul.assert_called_with(5, 100)

if __name__ == "__main__":
	unittest.main()
