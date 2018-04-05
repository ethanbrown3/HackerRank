# https://www.hackerrank.com/challenges/zipped/problem

# Input Format
# The first line contains  and  separated by a space. 
# The next  lines contains the space separated marks obtained by students in a particular subject.

N, X = map(int, raw_input().split())

scores = []
for _ in range(X):
    scores.append(map(float, raw_input().split()))

# print scores

# Loop through each list in the list returned by zip.
# i is a list of the ith term in each list.
for i in zip(*scores):
    # print i
    print sum(i)/len(i)
