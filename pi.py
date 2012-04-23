#!/usr/bin/python

from div import DecimalDiv
from sys import stdout

CACHE_SIZE = 10

class Pi:
	def __init__(self):
		# Lists contain DecimalDiv objects
		# Call .next() when needed
		self.atan5   = []
		self.atan239 = []

		# Current step (next DecimalDiv to create/append)
		self.atan5step   = 1
		self.atan239step = 1
		
		# List of last 10 digits found
		self.last10 = []
		
		# Current depth (number of decimal places)
		self.place = 0
		
		# Create the atan(1/5) generator
		d = DecimalDiv(16, self.atan5step * pow(5, self.atan5step), subtract=False)
		self.atan5.append(d)
		
		# Create the atan(1/239) generator
		d = DecimalDiv(4, self.atan239step * pow(239, self.atan239step), subtract=True)
		self.atan239.append(d)
	
	def add_list(self, lst, atan = 5):
		to_remove = []
		# Current number (value at current decimal place)
		result = 0
		for i, div in enumerate(lst):
			if div.place == self.place:
				if i == len(lst) - 1:
					if atan == 5:
						self.atan5step += 2
						step = self.atan5step
						mult = 16
					elif atan == 239:
						self.atan239step += 2
						step = self.atan239step
						mult = 4
					d = DecimalDiv(mult, 
								step * pow(atan, step),
								subtract = not div.subtract)
					lst.append(d)
					
				dec = div.next()
				if dec == None:
					to_remove.append(div)
				elif div.subtract:
					result -= dec
				else:
					result += dec
		for remove in to_remove:
			lst.remove(remove)
		return result

	def next(self):
		while len(self.last10) <= CACHE_SIZE:
			current  = self.add_list(self.atan5, atan=5)
			current += self.add_list(self.atan239, atan=239)
			self.last10.insert(0, current)
			self.place += 1
		
		for i in xrange(0, len(self.last10) - 1):
			while self.last10[i] >= 5:
				self.last10[i+1] += 1
				self.last10[i] -= 10
			while self.last10[i] < 0:
				self.last10[i+1] -= 1
				self.last10[i] += 10
		
		last = str(self.last10.pop(-1))
		return last

print ''
f = open('test.txt', 'r')
test = f.read()
f.close()

pi = Pi()
pistr = '3.'
for i in xrange(0, 2000):
	pistr += str(pi.next())
	stdout.write('.')
	stdout.flush()
print ''

for i in xrange(0, len(pistr)):
	stdout.write(pistr[i])
	if pistr[i] != test[i]:
		print "\nmismatched at character %d, %s should be %s" % (i + 1, pistr[i], test[i])
		break
print ''
exit(0)

