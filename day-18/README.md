# Day - 18
## ⭐️ Search Insert Position – 18.1
### 🔗 Problem

[LeetCode #35 – Search Insert Position](https://leetcode.com/problems/search-insert-position/)

### 🧠 Core Idea

Use binary search on the sorted array to find the target’s index.
If the target is found, return its index directly.
If not found, when the loop ends, the left pointer will indicate the correct insertion position to maintain the sorted order.

### 📊 Example

Input: `nums = [1, 3, 5, 6]`, `target = 2`

Output: 1 -> Insert before 3.

### ⏱️ Complexity

- Time: O(log n) – Binary search halves the search space each iteration

- Space: O(1) – Only constant variables used

👉 See full code in [search_insert_position.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-18/search_insert_position.py)

---

## ⭐️ First Bad Version – 18.2
### 🔗 Problem

[LeetCode #278 – First Bad Version](https://leetcode.com/problems/first-bad-version/)

### 🧠 Core Idea

Perform binary search on versions from 1 to n.
If isBadVersion(mid) returns true, record mid as a candidate and move left to check for an earlier bad version.
If it returns false, move right to search later versions.
The earliest recorded bad version is the answer.

### 📊 Example

Input: `n = 5`, `first bad = 4`

Output: 4 -> First bad version is 4.

### ⏱️ Complexity

- Time: O(log n) – Search space is halved each step

- Space: O(1) – Constant extra space

👉 See full code in [first_bad_version.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-18/first_bad_version.py)
