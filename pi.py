#!/usr/bin/python

from div import DecimalDiv
from sys import stdout

CACHE_SIZE = 7

class Pi:
	def __init__(self):
		# Lists contain DecimalDiv objects. These objects give individual
		# decimals for the atan(1/5) and atan(1/239) calculations.
		self.atan5   = []
		self.atan239 = []

		# The current step in the atan series.  The series adds
		# and subtracts from "n", which increases by 2 every step
		# i.e. 1/5, 3/5^3, 5/5^5, etc..
		self.atan5step   = 1
		self.atan239step = 1
		
		# List of last X digits calculated. This acts as a cache
		# of the most-recently calculated digits of PI. These digits
		# are subject to change due to left-to-right addition
		self.lastX = []
		
		# Current depth (current decimal place being calculated)
		self.place = 0
		
		# Create the atan(1/5) generator
		d = DecimalDiv(16, self.atan5step * pow(5, self.atan5step), subtract=False)
		self.atan5.append(d)
		
		# Create the atan(1/239) generator
		d = DecimalDiv(4, self.atan239step * pow(239, self.atan239step), subtract=True)
		self.atan239.append(d)
	
	
	"""
		Adds up all digits current in place at self.place,
		uses the DecimalDiv objects in the given "lst"
		Returns this resulting total.
		Also, creates new DecimalDiv objects as needed.
	"""
	def add_list(self, lst, atan = 5):
		to_remove = []
		result = 0
		# Iterate over every item in the list
		# Each item represents a piece of the atan(1/5) or 
		# atan(1/239) series. The items are is decreasing order
		for i, div in enumerate(lst):
			# We only care if the calculation is currently at the 
			# decimal place we are calculating
			if div.place == self.place:
				# Get the next digit, add to result
				# Remove DecimalDiv if it no longer produces digits (numerator became 0 and next() returned None)
				dec = div.next()
				if dec == None:
					to_remove.append(div)
				elif div.subtract:
					result -= dec
				else:
					result += dec
				
				# If this is the last item in the list, we need to 
				# create a new DecimalDiv to generate future digits
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
				
		# Remove "dead" DecimalDivs (no longer generating digits)
		# For example, 1/5 will generate 0.2 and that's it,
		# whereas 1/3 will generate 0.3333 infinitely
		for remove in to_remove:
			lst.remove(remove)
		return result

	"""
		Returns the next digit of PI
		Does not include the leading "3.", starts at "14159..."
	"""
	def next(self):
		# We will use lastX to hold the last X digits calculated
		# This is required as we are doing left-to-right addition
		# and previously-computed digits are subject to change
		# Example: first digit is 2 ("3.2") and next digit is (-5)
		# By propigating the -5, we end up with "3.15", and the 2
		# ended up changing.
		while len(self.lastX) <= CACHE_SIZE:
			# Add everything in the atan(1/5) and atan(1/239) series
			# Only adds decimals from these series that are currently
			# at the same place we are calculating.
			current  = self.add_list(self.atan5, atan=5)
			current += self.add_list(self.atan239, atan=239)
			self.lastX.insert(0, current)
			self.place += 1
		
		# Digits should be between 0 and 9.
		# It's possible the addition of digits are negative or >10
		# So we have to propigate the carry-over down the cache.
		for i in xrange(0, len(self.lastX) - 1):
			# If number is greater than 10, propigation increases
			# the previous digit
			while self.lastX[i] >= 10:
				self.lastX[i+1] += 1
				self.lastX[i] -= 10
			# If number is negative, propigation decreases the
			# previous digit
			while self.lastX[i] < 0:
				self.lastX[i+1] -= 1
				self.lastX[i] += 10
		
		# Once the cache is full, remove the last item (FIFO)
		last = self.lastX.pop(-1)
		return last


########
# TEST #
########

# Open file containing first 100k digits of pi, for comparison
f = open('test.txt', 'r')
test = f.read()
f.close()

# Create Pi object which will generate the digits
pi = Pi()
pistr = '3.'
stdout.write('3.')
#for i in xrange(0, 1000):
i = 0
while True:
	# Get the next digit
	pistr = str(pi.next())
	# Print it
	stdout.write(pistr)
	stdout.flush()
	# Compare with the precomputed 100k digits to ensure 
	# we are calculating the correct digits
	if len(test) > i - 3 and pistr != test[i + 2]:
		# If inconsistent, show digit number and display info
		print "\nmismatched at character %d, %s should be %s" % (i + 1, pistr, test[i + 2])
		break
	i += 1

print ''
exit(0)

