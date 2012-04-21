#!/usr/bin/python

from div import DecimalDiv
from sys import stdout

# Lists are full of DecimalDiv
# Call .next() when needed
atan5   = []
atan239 = []

# Current step (next DecimalDiv to create/append)
atan5step   = 3
atan239step = 1

# Previous number, in case current-total >= 10
# We may need to change previous decimal
# 3.2 - 0.0.426 = 3.15...
prev = 3
place = 0

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
	if count > 50: break
print '',

