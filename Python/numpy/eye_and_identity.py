# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy
numpy.set_printoptions(sign=' ')
n, m = map(int, raw_input().split())

print numpy.eye(n, m)