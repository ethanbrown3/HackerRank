# https://www.hackerrank.com/challenges/exceptions/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for i in range(0, N):
    a = [i for i in raw_input().split()]
    try:
        print int(a[0])/int(a[1])
    except (ZeroDivisionError, ValueError) as err:
        print 'Error Code:', str(err)
