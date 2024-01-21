#!/bin/python

import math
import os
import random
import re
import sys

# Solution
def solution(n, x, costs, quantity):
    arrf=[[costs[i],quantity[i]] for i in range(n)]
    arrf.sort()
    i=0
    c=0
    while(x>0 and i<len(arrf)):
        canspend=(x//arrf[i][0])
        count=(min(arrf[i][1],canspend))
        x=(x-(count*arrf[i][0]))
        c+=count
        i+=1
    return (c//3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        x = int(raw_input().strip())

        arr1 = map(int, raw_input().rstrip().split())

        arr2 = map(int, raw_input().rstrip().split())

        ans = solution(n, x, arr1, arr2)

        fptr.write(str(ans) + '\n')

    fptr.close()
