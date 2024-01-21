#!/bin/python

import math
import os
import random
import re
import sys

#Solution
def solution(S):
    return (S//2)**2






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        S = int(raw_input().strip())

        ans = solution(S)

        fptr.write(str(ans) + '\n')

    fptr.close()
