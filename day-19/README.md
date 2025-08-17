# Day - 19 
## ⭐️ Sqrt(x) – 19.1
### 🔗 Problem

[LeetCode #69 – Sqrt(x)](https://leetcode.com/problems/sqrtx/)

### 🧠 Core Idea

The integer square root lies between 0 and x. Use binary search to find the largest mid such that mid * mid <= x. 
If mid * mid == x, return mid; otherwise keep the best candidate and shrink the range accordingly. 
The final answer is the floor of the true square root.

### 📊 Example

Input: `x = 8`

Output: 2 -> sqrt(8) = 2.828…, floor is 2.

### ⏱️ Complexity

- Time: O(log n) – Search range halves each step

- Space: O(1) – Constant extra space

👉 See full code in [sqrtx.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-19/sqrt_x.py)

---

## ⭐️ Valid Perfect Square – 19.2
### 🔗 Problem

[LeetCode #367 – Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

### 🧠 Core Idea

A perfect square has an integer root k with k * k = num. 
Run binary search on [1, num] (or [1, num//2] for num >= 2) and check mid * mid against num. 
Exact match returns true; otherwise move left/right accordingly. If the loop ends without a match, return false.

### 📊 Example

Input: num = 16 -> Output: true

Input: num = 14 -> Output: false

### ⏱️ Complexity

- Time: O(log n) – Logarithmic checks

- Space: O(1) – No extra data structures

👉 See full code in [valid_perfect_square.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-19/valid_perfect_square.py)
