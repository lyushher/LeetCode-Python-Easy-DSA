# Day - 05
## ⭐️ Merge Sorted Array – 5.1
### 🔗 Problem
[LeetCode #88 – Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

### 🧠 Core Idea
Start merging from the end of nums1 to avoid overwriting existing elements.
Use two pointers to compare values from the back of both arrays and insert the larger one at the end.
This enables in-place merging without using extra memory.

### 📊 Example
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: nums1 = [1,2,2,3,5,6]

### ⏱️ Complexity
- Time: O(n + m) – One pass over both arrays

- Space: O(1) – In-place merge without extra space

👉 See full code in [merge_sorted_array.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-05/merged_sorted_array.py)

---

## ⭐️ Plus One – 5.2
### 🔗 Problem
[LeetCode #66 – Plus One](https://leetcode.com/problems/plus-one/description/)

### 🧠 Core Idea
Traverse the digits from the end and simulate addition with carry.
If a digit is 9, set it to 0 and carry over; otherwise, increment and return immediately.
If all digits were 9, add 1 at the front by returning [1] + digits.

### 📊 Example
Input: digits = [9,9,9]

Output: [1,0,0,0] - Because 999 + 1 = 1000

### ⏱️ Complexity
- Time: O(n) – Single pass through the digits

- Space: O(1) – Ignoring the output array size

👉 See full code in [plus_one.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-05/plus_one.py)
