# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy
numpy.set_printoptions(sign=' ')
n, m = raw_input().split()
n = int(n)
m = int(m)
print numpy.eye(n, m)