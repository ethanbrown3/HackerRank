#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]
    high_records = 0
    low_records = 0
    low = scores[0]

    for s in scores:
        if s > high:
            high_records += 1
            high = s
        if s < low:
            low_records += 1
            low = s

    high_records = str(high_records)
    low_records = str(low_records)
    return high_records + ' ' + low_records

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(raw_input())

#     score = map(int, raw_input().rstrip().split())

#     result = breakingRecords(score)

#     fptr.write(result)
#     fptr.write('\n')

#     fptr.close()


if __name__ == '__main__':
    fptr = open('output', 'w')

    # n = int(raw_input())

    # score = map(int, raw_input().rstrip().split())
    f = open('code_sprints/input.txt', 'r') 
    score = map(int, f.readlines()[0].split())
    result = breakingRecords(score)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()