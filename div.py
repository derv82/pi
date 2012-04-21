#!/usr/bin/python
from math import log
print int(log(5, 10))


"""
	Big number division (x/y)
	Detects repeating decimals and places into brackets.
	Returns a String.
	div(4, 2) returns "2"
	div(1, 3) returns "0.(3)"
	div(-1, 1) returns "-1"
"""
def div(x, y, max_length = 500):
	if y == 0:
		return "DIVIDE BY ZERO"
	sign = ""
	if (x < 0) != (y < 0):
		sign = "-"
	x = abs(x)
	y = abs(y)
	result = ""
	hit_decimal = False
	while True:
		quotient = 0
		while x >= y:
			quotient += 1
			x -= y
		result += str(quotient)
		print result
		
		if x == 0.0:
			break
		
		if x < y:
			x *= 10
			if not hit_decimal:
				hit_decimal = True
				result += '.'
		if '.' in result:
			prev = ""
			dec = result[result.find('.')+1:]
			index = len(dec)
			while len(dec) > 0:
				if len(dec) > 0 and len(dec) % 9 == 0:
					match = True
					for m in xrange(1, 9):
						for n in xrange(0, len(dec) / 9):
							if dec[n] != dec[(m*len(dec)/9)+n]:
								match = False
								break
						if not match: break
					if match:
						repeating = dec[0:len(dec) / 9]
						if repeating != '0' * len(repeating):
						#	return sign + result[:result.find('.')+1] + prev
						#else:
							return sign + result[:result.find('.')+1] + prev + "(" + dec[0:len(dec) / 9] + ")"
				prev += dec[0]
				dec = dec[1:]
		if len(result) > max_length: break
	
	return sign + result

(x, y) = (1, pow(5.0, 20) * 20)
print x, "/", y, "=", div(x, y)
exit(0)
(x, y) = (1, pow(239, 5) * 5)
print x, "/", y, "=", div(x, y)
exit(0)
(x, y) = (1, 1)
print x, "/", y, "=", div(x, y)
(x, y) = (6, 2)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 5)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 9)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 50)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 500)
print x, "/", y, "=", div(x, y)
(x, y) = (35, 5)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 239)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 11)
print x, "/", y, "=", div(x, y)
(x, y) = (3227, 555)
print x, "/", y, "=", div(x, y)
(x, y) = (7, 12)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 81)
print x, "/", y, "=", div(x, y)
(x, y) = (22, 7)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 17)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 19)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 23)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 29)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 97)
print x, "/", y, "=", div(x, y, max_length=1000)
(x, y) = (1, 47)
print x, "/", y, "=", div(x, y)
(x, y) = (1, 49)
print x, "/", y, "=", div(x, y)
(x, y) = (46, 55)
print x, "/", y, "=", div(x, y)
(x, y) = (-1, 10)
print x, "/", y, "=", div(x, y)
(x, y) = (1, -10)
print x, "/", y, "=", div(x, y)
(x, y) = (-1, -10)
print x, "/", y, "=", div(x, y)
(x, y) = (-1, 1)
print x, "/", y, "=", div(x, y)
