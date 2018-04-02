# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(raw_input())
shoes = Counter(map(int, raw_input().split()))

n = int(raw_input())

total = 0
for i in range(n):
    purchase = raw_input().split()
    purchase = map(int, purchase)
    if shoes[purchase[0]]:
        total += purchase[1]
        shoes[purchase[0]] -= 1
print total
    