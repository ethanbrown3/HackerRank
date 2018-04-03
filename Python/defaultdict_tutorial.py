# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# d['python'].append("awesome")

from collections import defaultdict
d = defaultdict(list)
l = []

n, m = map(int, raw_input().split())

for i in range(0, n):
    d[raw_input()].append(i + 1)

for i in range(0, m):
    l += [raw_input()]

print d
print l

for i in l:
    if i in d:
        print " ".join(map(str, d[i]))
    else:
        print -1
