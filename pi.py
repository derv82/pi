#!/usr/bin/python

from div import DecimalDiv
from sys import stdout

# Lists contain DecimalDiv objects
# Call .next() when needed
atan5   = []
atan239 = []

# Current step (next DecimalDiv to create/append)
atan5step   = 1
atan239step = 1

# List of last 10 digits found
last10 = []

# Current depth (number of decimal places)
place = 0

d = DecimalDiv(16, atan5step * pow(5, atan5step), subtract=False)
atan5.append(d)

d = DecimalDiv(4, atan239step * pow(239, atan239step), subtract=True)
atan239.append(d)

def add_digit(digit, sign):
	if sign:
		current += digit
	else:
		current -= digit
	

PI = '3.'
stdout.write('3.')
while True:
	to_remove = []
	# Current number (value at current decimal place)
	current = 0
	for i, div in enumerate(atan5):
		if div.place == place:
			if i == len(atan5) - 1:
				atan5step += 2
				d = DecimalDiv(16, 
							atan5step * pow(5, atan5step),
							subtract = not div.subtract)
				atan5.append(d)
				
			i5 = div.next()
			if i5 == None:
				to_remove.append(div)
			elif div.subtract:
				current -= i5
			else:
				current += i5
	for remove in to_remove:
		atan5.remove(remove)
	
	to_remove = []
	for i, div in enumerate(atan239):
		if div.place == place:
			if i == len(atan239) - 1:
				atan239step += 2
				d = DecimalDiv(4, 
							atan239step * pow(239, atan239step),
							subtract = not div.subtract)
				atan239.append(d)
		
			i239 = div.next()
			if i239 == None:
				to_remove.append(div)
			elif div.subtract:
				current -= i239
			else:
				current += i239
	for remove in to_remove:
		atan239.remove(remove)
	
	last10.insert(0, current)
	for i in xrange(0, len(last10) - 1):
		while last10[i] >= 5:
			last10[i+1] += 1
			last10[i] -= 10
		while last10[i] < 0:
			last10[i+1] -= 1
			last10[i] += 10
	
	if len(last10) > 10:
		last = str(last10.pop(-1))
		PI += last
		stdout.write(last)
		stdout.flush()
	
	current = 0
	place += 1
	if place > 50:
		break
	
	# Remove two decimal generators if they are both repeating
  # the same number and their signs are opposite (add/sub)
	# Disabled because it's useless?
	"""
	if place % 25:
		for i in xrange(0, len(atan5) - 1):
			for j in xrange(i + 1, len(atan5)):
				if atan5[i].repeating != None and atan5[i].repeating == atan5[j].repeating and atan5[i].subtract != atan5[j].subtract:
					atan5.pop(i)
					i -= 1
					atan5.pop(j)
					j -= 2
	"""


print ''
f = open('test2.txt', 'r')
test = f.read()
f.close()
for i in xrange(0, len(PI)):
	stdout.write(PI[i])
	if PI[i] != test[i]:
		print "\nmismatched at character %d, %s should be %s" % (i + 1, PI[i], test[i])
		break
exit(0)

