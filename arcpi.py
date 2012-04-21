#!/usr/bin/py

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

