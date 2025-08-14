# Problem: Fibonacci Number  
# Link: https://leetcode.com/problems/fibonacci-number/  
# Tags: Dynamic Programming, Math  
# Approach: Use two variables to iteratively calculate the Fibonacci sequence, starting from F(0) = 0 and F(1) = 1.  
# Time Complexity: O(n)  
# Space Complexity: O(1) – constant space for two variables  


class Solution:
    def fib(self, n):
        a, b = 0, 1 
        for _ in range(n):
            a, b = b, a + b
        return a
