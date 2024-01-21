# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/find-maximum-product-given-sum-1](url)

# Approach

## Pre requisites
1. Math

## Brute force
1. We can try to find the product of all X.(S-X) , where X goes from 1 to S-1.
2. But Time complexity will go to O(S).
3. Is there an optimal way to do this?

## Optimal solution - math 
1. It is known that, given sum X+Y=S, the maximum product X.Y occurs if X and Y are both S/2.
2. It is one of the very first thing we prove in calculus!
3. Proof: [https://math.stackexchange.com/a/3074692](url)
4. Time complexity: O(1)
