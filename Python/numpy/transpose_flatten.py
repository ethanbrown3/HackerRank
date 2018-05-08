# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy
n = raw_input().split()
n = list(map(int, n))

l = []
for x in range(n[0]):
    arrin = raw_input().split()
    arrin = list(map(int, arrin))
    l.append(arrin)

l = numpy.array(l)
print numpy.transpose(l)
print l.flatten()