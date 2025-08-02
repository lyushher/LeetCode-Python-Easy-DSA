# Day - 04

## ⭐️ Single Number – 4.1
### 🔗 Problem
[LeetCode #136 – Single Number](https://leetcode.com/problems/single-number/description/)

### 🧠 Core Idea
Use XOR to cancel out duplicates, leveraging `a ^ a = 0` and `a ^ 0 = a`.
As all duplicate numbers cancel each other, only the unique number remains after a single pass.

### 📊 Example
Input: nums = [4,1,2,1,2]

Output: 4 → Because every number appears twice except 4

### ⏱️ Complexity
Time: O(n) – One pass to XOR all elements

Space: O(1) – Only one variable used

👉 See full code in [single_number.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-04/single_number.py)

## ⭐️ Missing Number – 4.2
### 🔗 Problem
[LeetCode #268 – Missing Number](https://leetcode.com/problems/missing-number/)

### 🧠 Core Idea
XOR all indices and values to eliminate matching pairs, using the identity `a ^ a = 0`.
Since the complete range [0, n] should be present, the only unmatched value left is the missing number.

### 📊 Example
Input: nums = [3,0,1]

Output: 2 → Because range is [0,3], and 2 is missing

### ⏱️ Complexity
Time: O(n) – One pass to XOR indices and values

Space: O(1) – Constant space usage

👉 See full code in [missing_number.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-04/missing_number.py)

