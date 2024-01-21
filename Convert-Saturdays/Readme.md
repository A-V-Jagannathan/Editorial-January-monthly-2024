# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/convert-saturdays](url)

# Approach
1. We have to make sure everyday's frequency is equal.
2. And we have to find minimum number, to add to each day to make every-day's frequency equal.
3. Since we cannot delete, we have to take a greedy approach.
4. Find out the maximum frequency among the days, and find out how many saturdays to convert for each day to reach the desired frequency.
5. Sum them up for answer!

# Time and space complexity

Both O(1) per test-case (Since number of days are fixed (5), it is not O(n) for finding max)
