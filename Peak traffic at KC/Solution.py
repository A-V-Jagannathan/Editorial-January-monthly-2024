#!/bin/python

import math
import os
import random
import re
import sys

#Solution
def solution(n, A, time):
    leaving_time= [A[i]+time[i] for i in range(n)]
    events=[]
    
    for i in range(n):
        events.append([A[i],1])
        events.append([leaving_time[i],-1])
    events.sort()
    
    maxcount=0
    count=0
    for i in range(len(events)):
        count+=events[i][1]
        maxcount=max(count,maxcount) 
    return maxcount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr1 = map(long, raw_input().rstrip().split())

    arr2 = map(long, raw_input().rstrip().split())

    ans = solution(n, arr1, arr2)

    fptr.write(str(ans) + '\n')

    fptr.close()
