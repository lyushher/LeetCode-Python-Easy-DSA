# Day - 08
## ⭐️ Valid Parentheses – 8.1
### 🔗 Problem
[LeetCode #20 – Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### 🧠 Core Idea
Use a stack to keep track of opening brackets while scanning through the string.
Each time a closing bracket appears, check whether it correctly matches the most recent opening bracket.
The string is valid only if the stack is empty after processing all characters.

### 📊 Example
Input: `s = "()[]{}"`

Output: true → Because every opening bracket has a valid matching closing bracket

### ⏱️ Complexity
- Time: O(n) – One pass through the string

- Space: O(n) – Stack space in the worst case

👉 See full code in [valid_parentheses.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-08/valid_parentheses.py)

---

## ⭐️ Remove Duplicates from Sorted Array – 8.2
### 🔗 Problem
[LeetCode #26 – Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

### 🧠 Core Idea
Use two pointers to iterate through the array while tracking the last placed unique value.
Whenever a new unique number is encountered, place it at the next write position and increment the counter.
The function returns the length of the updated array segment with all unique elements in-place.

### 📊 Example
Input: `nums = [1,1,2]`

Output: 2 → Because the array becomes [1,2,_] with the first 2 values being unique

### ⏱️ Complexity
- Time: O(n) – One pass through the array

- Space: O(1) – In-place with constant space

👉 See full code in [remove_duplicates.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-08/remove_duplicates_from_sorted_array.py)
