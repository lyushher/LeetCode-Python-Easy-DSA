# Day 28

## ⭐️ Longest Common Prefix – 28.1
### 🔗 Problem
[LeetCode #14 – Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

### 🧠 Core Idea
Choose the first word as a baseline and compare its characters across all other words, stopping when a mismatch is found or one of the words ends.
The substring up to that point is the longest common prefix.
This ensures we only check as far as characters match, giving an efficient early termination strategy.

### 📊 Example
Input: strs = \["flower","flow","flight"]

Output: `"fl"`

### ⏱️ Complexity
- Time: O(S) – where S is the total number of characters across all strings (early exit possible)

- Space: O(1) – Constant space usage

👉 See full code in [longest_common_prefix.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-28/longest_common_prefix.py)

---

## ⭐️ Keyboard Row – 28.2
### 🔗 Problem
[LeetCode #500 – Keyboard Row](https://leetcode.com/problems/keyboard-row/)

### 🧠 Core Idea
Each keyboard row can be represented as a set of letters. 
For each word, convert its letters into a set and check if it is a subset of any row set.
If yes, the word can be typed using letters from one row only.

### 📊 Example
Input: words = \["Hello","Alaska","Dad","Peace"]

Output: \["Alaska","Dad"]

### ⏱️ Complexity
- Time: O(n·k) – n = number of words, k = average length of each word

- Space: O(1) – Only three row sets used

👉 See full code in [keyboard_row.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-28/keyboard_row.py)
