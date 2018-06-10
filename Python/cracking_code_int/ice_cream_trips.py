#!/bin/python
'''
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
'''
# Complete the solve function below.
def solve(arr, money):
    no_flavors = len(arr)
    memo = {}
    out = []
    for i in range(no_flavors):
        if money-arr[i] in memo:
            out.append(i)
            out.append(memo[money-arr[i]])
            break
        memo[arr[i]] = i

    print ' '.join([str(i+1) for i in sorted(out)])
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        solve(arr, money)
