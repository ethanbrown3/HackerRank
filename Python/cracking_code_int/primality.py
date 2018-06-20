#!/bin/python
'''
https://www.hackerrank.com/challenges/ctci-big-o/problem
Since for every non-prime number that has a factor bigger than sqrt(n) there
is a factor smaller, we can limit our for loop to sqrt(n) + 1 to avoid
extra iterations. This will bring the complexity down to O(sqrt(n)),
'''
import math

def is_prime(num):
    result = 'Prime'
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i) == 0:
                result = 'Not prime'
                break
    else:
        result = "Not prime"
    print result

if __name__ == '__main__':
    p = int(raw_input())

    for p_itr in xrange(p):
        n = int(raw_input())
        is_prime(n)
