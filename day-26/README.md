# Day 26 

## ⭐️ Move Zeroes – 26.1
### 🔗 Problem
[LeetCode #283 – Move Zeroes](https://leetcode.com/problems/move-zeroes/)

### 🧠 Core Idea
Use a two-pointer approach to shift all non-zero elements forward while maintaining their relative order. 
One pointer (last_non_zero) marks the next position to place a non-zero, while the other scans through the array. 
After placing all non-zero values, fill the remaining positions with zeros. 
This ensures the operation is in-place and preserves order.

### 📊 Example
Input: `nums = [0,1,0,3,12]`

Output: [1,3,12,0,0]

### ⏱️ Complexity
- Time: O(n) – Single pass through the array plus one pass to fill zeros

- Space: O(1) – In-place, no extra structures

👉 See full code in [move_zeroes.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-26/move_zeroes.py)

---

## ⭐️ Find All Numbers Disappeared in an Array – 26.2
### 🔗 Problem
[LeetCode #448 – Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

### 🧠 Core Idea
Since numbers are within the range [1, n], we can mark visited indices by flipping the sign of the element at abs(x) - 1.
After one pass, the indices that remain positive indicate the missing numbers.
Collect those indices + 1 as the result.
This avoids extra memory usage and leverages in-place marking.

### 📊 Example
Input: `nums = [4,3,2,7,8,2,3,1]`

Output: [5,6] -> Because 5 and 6 are not present in the array

### ⏱️ Complexity
- Time: O(n) – Single pass to mark and one pass to collect
- 
- Space: O(1) – In-place marking (excluding output list)

👉 See full code in [find_all_numbers_disappeared_in_an_array.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-26/find_all_numbers_disappeared_in_an_array.py)
