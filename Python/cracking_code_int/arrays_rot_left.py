#!/bin/python
'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
Using index slicing makes this really simple. Just append the right half
from the number of rotations as the index to the left half
    d = 4
    1 2 3 4 | 5
    5 +|+ 1 2 3 4

    d = 2
    1 2 | 3 4 5
    3 4 5 +|+ 1 2
'''

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open('output', 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)
    result = ' '.join(map(str, result))
    fptr.write(result)
    fptr.write('\n')

    fptr.close()
