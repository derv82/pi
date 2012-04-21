#!/usr/bin/python

"""	
	Convert two strings to similar formatting.
	Makes addition much easier.
"""
def equalize(x, y):
	x = str(x)
	y = str(y)
	x_dot = x.find('.')
	if x_dot == -1: 
		x_dot = len(x)
	y_dot = y.find('.')
	if y_dot == -1:
		y_dot = len(y)
	
	i = 0
	
	rdepthx = (x[x_dot+1:])
	ldepthx = (x[:x_dot])
	rdepthy = (y[y_dot+1:])
	ldepthy = (y[:y_dot])

	while len(rdepthx) < len(rdepthy):
		rdepthx = rdepthx + "0"
	while len(rdepthy) < len(rdepthx):
		rdepthy = rdepthy + "0"
	while len(ldepthx) < len(ldepthy):
		ldepthx = "0" + ldepthx
	while len(ldepthy) < len(ldepthx):
		ldepthy = "0" + ldepthy
	
	return (ldepthx + "." + rdepthx, ldepthy + "." + rdepthy)

def add(x, y):
	(x,y) = equalize(x, y)
	z = [None] * len(x)
	print z
	print x, '\n', y
	
	for i in xrange(len(x) - 1, 0, -1):
		print i, x[i], y[i]
		z[i] = x[i] + y[i]
		if z[i] > 10:
			x[i-1] = int(x[i-1]) + int(z[i]) - 10
			z[i] = int(z[i]) - 10
	
	print '-' * 20
	print z
	
add("5000", "1.0382")
add(5000, 1.0389)
