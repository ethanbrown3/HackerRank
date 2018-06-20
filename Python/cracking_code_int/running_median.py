#!/bin/python
'''
https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
This required a faster way to sort the list. So rather than inserting an element on
the end of the list then sorting we use the bisect module to run insort_left.
insort takes a list and an element. It then will insert the element in the correct
sorted position. This avoids having to run a sorting algorithm on the list.
'''
import bisect

def get_median(mylist):
    length = len(mylist)
    if not length % 2:
        return (mylist[length / 2] + mylist[length / 2 - 1]) / 2.0
    return mylist[length / 2]

if __name__ == '__main__':
    n = int(raw_input())

    a = []
    for _ in xrange(n):
        a_item = int(raw_input())
        bisect.insort_left(a, a_item)
        print float(get_median(a))
        
