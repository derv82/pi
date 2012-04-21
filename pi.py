#!/usr/bin/python

class ATan:
	def __init__(self, number):
		self.number = 1 / float(number)
		self.subtract = False
		self.result = 0
		self.iteration = 1
	
	def next(self):
		exp = float(pow(self.number, self.iteration))
		exp /= float(self.iteration)
		if self.subtract:
			self.result -= exp
		else:
			self.result += exp
		self.subtract = not self.subtract
		self.iteration += 2
		
		return self.result

atan5 = ATan(5)
atan239 = ATan(239)

for x in xrange(0, 10):
	print 16 * atan5.next() - 4 * atan239.next()
exit(0)



def arctan(x, iterations):
  result = 0
  subtract = False
  total_iterations = iterations * 2
  for iter in xrange(1, total_iterations, 2):
    exp = float(pow(x, iter))
    if subtract:
      result -= (exp / float(iter))
    else:
      result += (exp / float(iter))
    subtract = not subtract
  return result
 
its = 5
pi = 16 * arctan(1 / float(5), its) - 4 * arctan(1 / float(239), its)
print pi

