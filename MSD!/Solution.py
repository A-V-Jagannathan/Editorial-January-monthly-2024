#!/bin/python

import math
import os
import random
import re
import sys

# Solution
def solution(s):
    summ=0
    for i in s:
        summ+=ord(i)
    if(summ%7==0):
        return "THALA FOR A REASON"
    else:
        return "IAM SAD"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        s = raw_input()

        ans = solution(s)

        fptr.write(ans + '\n')

    fptr.close()
