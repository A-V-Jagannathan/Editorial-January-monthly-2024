# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/find-maximum-product-given-sum](url)
# Approach
1. It can be observed that, regardless of value of X and Y, their product will always be negative, because Y is negative and X is positive.
2. So we want to minimize the absolute value of X.Y to get the maximum product ( Why?-> because -(a)>-(a+1) )
3. For that, there will be 2 cases, when X+Y>=0 and X+Y<0
4. Case 1, S>=0: we can take X to be S+1 and Y to -1. So product will be -(S+1). This will be the max product.
5. Case2, S<0: we can take X to be 1 and Y to be S-1. So product will be S-1. This will be the max product.

# Time and space complexity
Both O(1).

