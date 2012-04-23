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
	

stdout.write('3.')
while True:
	to_remove = []
	# Current number (value at current decimal place)
	current = 0
	for i, div in enumerate(atan5):
		# If we are at the end of the list,
		# and the last item's decimal place is
		# at our current position,
		if i == len(atan5) - 1 and div.place == place:
			#print "created atan5(%d)" % atan5step
			atan5step += 2
			d = DecimalDiv(16, 
						atan5step * pow(5, atan5step),
						subtract = not div.subtract)
			atan5.append(d)
		
		if div.place == place:
			i5 = div.next()
			if i5 == None:
				to_remove.append(div)
			elif div.subtract:
				current -= i5
				#print "-%d (5)" % i5
			else:
				current += i5
				#print "+%d (5)" % i5
				#stdout.write("  5/%d: %d" % (div.place, i5))
				#raw_input()
	for remove in to_remove:
		atan5.remove(remove)
	
	to_remove = []
	for i, div in enumerate(atan239):
		# If we are at the end of the list,
		# and the last item's decimal place is
		# at our current position,
		if i == len(atan239) - 1 and div.place == place:
			#print "created atan239(%d)" % atan239step
			atan239step += 2
			d = DecimalDiv(4, 
						atan239step * pow(239, atan239step),
						subtract = not div.subtract)
			atan239.append(d)
		
		if div.place == place:
			i239 = div.next()
			if i239 == None:
				to_remove.append(div)
			elif div.subtract:
				current -= i239
				#print "-%d (239)" % i239
			else:
				current += i239
				#print "+%d (239)" % i239
				#stdout.write("239/%d: %d" % (div.place, i239))
				#raw_input()
	for remove in to_remove:
		atan239.remove(remove)
	
	last10.insert(0, current)
	for i in xrange(0, len(last10) - 1):
		while last10[i] >= 10:
			last10[i+1] += 1
			last10[i] -= 10
		while last10[i] < 0:
			last10[i+1] -= 1
			last10[i] += 10
	
	if len(last10) >= 11:
		last = last10.pop(-1)
		stdout.write(str(last))
		#raw_input()
	
	current = 0
	place += 1
	if place > 50:
		break

print ''
exit(0)

# Testing DecimalDiv
n = 15
d = DecimalDiv(16, n * pow(5, n))

print "zeros:", d.leading_zeros

x = d.next()
count = 0
while x != None:
	#stdout.write(str(x))
	#stdout.flush()
	print x, d.place
	x = d.next()
	count += 1
	if count > 15: break
print '',

