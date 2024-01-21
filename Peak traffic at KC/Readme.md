# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/peak-traffic-at-kc](url)
# Approach

## Idea
1. We are interested only in the arrival and leaving times of students and **not interested in when student_i arrived and left**
2. Why/What? Suppose 3 students are inside KC right now at time t. In t+1, one leaves. We know the number of students currently inside is 2.
3. Notice that it did not matter who left, and only the **event of entering/leaving KC matters** .

## Solution
1. We can denote the event of entering as {entering_time_i, +1} and leaving as {leaving_time_i, -1}.
2. Combine them into a single array.
3. Sort it based on time so the events are sorted
4. Eg. { {0,1} , {1,1} , {2,-1} , {3,1} , {4,-1}, {5,-1}} , says that t=0 someone entered , t=1 someone entered and so on..
5. Maintain sum and ans, keep adding 2nd element to sum and at each i, ans=max(ans,sum)


## Time and space complexity

TC: O(nlogn) for Sorting

SC: O(n) for storing array.

## Further resources

1. https://cses.fi/problemset/task/1619
   
