#!/usr/bin/python

from sys import stdout
import math

"""
	Yields next decimal place of a division
	Ignores leading whole integers; only
	cares about what's after the decimal point
"""
class DecimalDiv:
	def __init__(self, numerator, denom, subtract = True):
		self.x = numerator
		self.y = denom
		self.subtract = subtract
		self.place = 0
		while self.x > self.y:
			self.x -= self.y
	
	"""
		Returns number of leading zeros in decimal
	"""
	def count_zeros(self):
		# log is unreliable (e.g. when n = 13)
		# return math.floor(math.log(self.y, self.x))
		zeros = 0
		while self.x * 10 < self.y:
			self.x *= 10
			zeros += 1
		return zeros
	
	
	"""
		Returns None when there is nothing 
		left to divide (numerator is 0)
	"""
	def next(self):
		if self.x == 0:
			return None
		
		quotient = 0
		if self.x < self.y:
			self.x *= 10
		
		# The actual division happens here
		while self.x >= self.y:
			quotient += 1
			self.x -= self.y
		
		return quotient

def test():
	n = 11
	d = DecimalDiv(16, n * pow(5, n))
	x = d.next()
	while x != None:
		stdout.write(str(x))
		stdout.flush()
		x = d.next()
	print '',

if __name__ == '__main__':
	test()
