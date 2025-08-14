# Day - 16
## ⭐️ Fibonacci Number – 16.1
### 🔗 Problem

[LeetCode #509 – Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

### 🧠 Core Idea

Iteratively compute the n-th Fibonacci number using two variables to track the previous two values (F(n-2) and F(n-1)).
Start with F(0) = 0 and F(1) = 1, and loop from 2 to n, updating values in-place.
This bottom-up approach avoids the overhead of recursion and ensures linear time with constant space.

### 📊 Example

Input: `n = 4`

Output: 3 -> Because F(4) = F(3) + F(2) = 2 + 1 = 3

### ⏱️ Complexity

- Time: O(n) – Single loop from 2 to n

- Space: O(1) – No extra data structures used

👉 See full code in [fibonacci_number.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-16/fibonacci_number.py)

---

## ⭐️ Binary Search – 16.2
### 🔗 Problem

[LeetCode #704 – Binary Search](https://leetcode.com/problems/binary-search/)

### 🧠 Core Idea

Perform a standard binary search on a sorted array.
Maintain two pointers (left and right), calculate the middle index, and adjust the search boundaries based on comparison.
Efficiently narrows down the target location in logarithmic time.

### 📊 Example

Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

Output: 4 -> Because nums[4] is 9

### ⏱️ Complexity

- Time: O(log n) – Halves the search space each step

- Space: O(1) – Iterative implementation, no recursion stack

👉 See full code in [binary_search.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-16/binary_search.py)
