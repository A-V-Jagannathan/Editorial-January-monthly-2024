import math
import os
import random
import re
import sys

# Solution
def solution(days):
    maxx=max(days)
    summ=0
    for i in days:
        summ+=(maxx-i)
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):

        arr = map(int, raw_input().rstrip().split())

        ans = solution(arr)

        fptr.write(str(ans) + '\n')

    fptr.close()
