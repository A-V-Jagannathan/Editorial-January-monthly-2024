#!/bin/python

import math
import os
import random
import re
import sys

#Solution
def solution(S):
    if(S<0):
        return (S-1)*1
    else:
        return (S+1)*-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        S = int(raw_input().strip())

        ans = solution(S)

        fptr.write(str(ans) + '\n')

    fptr.close()
