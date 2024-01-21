# Problem link
[https://www.hackerrank.com/contests/january-monthly/challenges/maximum-days-you-can-skip-mess](url)
# Approach
1. Since you are only interested in buying as many snacks as possible with the money you have, You will take a greedy approach buying the least-cost items first.
2. At each point, we have to know the minimum cost item and the quantity of it.
3. For that, we can combine cost and quantity into a single 2D array of {cost_i,quantity_i} and sort it based on quantity.
4. At each i, you can buy a maximum of cost_i//remaining_money amount of item i. But the quantity_i can be less than this amount.
5. So you add c=min(cost_i//remaining_money, quantity_i) to the total snacks you have currently and reduce your money by c*cost_i

# Time complexity
Time complexity : O(nlogn) (Sort)

Space complexity : O(n) , for storing the arrays.
