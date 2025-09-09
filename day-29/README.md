# Day 29

## ⭐️ Longest Substring Without Repeating Characters – 29.1
### 🔗 Problem
[LeetCode #3 – Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### 🧠 Core Idea
Maintain a sliding window with two pointers and a hash map to track the last seen index of each character. 
When a duplicate is found inside the current window, move the left pointer just past the previous occurrence to keep the substring unique. 
Continuously update the maximum window length as you expand the right pointer.

### 📊 Example
Input: `s = "abcabcbb"`

Output: `3` -> Longest substring is `"abc"`

### ⏱️ Complexity
- Time: O(n) – Each character is processed at most twice

- Space: O(k) – At most one entry per unique character

👉 See full code in [longest_substring_without_repeating_characters.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-29/longest_substring_without_repeating_characters.py)

---

## ⭐️ Summary Ranges – 29.2
### 🔗 Problem
[LeetCode #228 – Summary Ranges](https://leetcode.com/problems/summary-ranges/)

### 🧠 Core Idea
Track the start of each range while scanning the array.
Whenever consecutive order breaks, record the range as either a single number or a "start->end" string, then reset the start.
After the loop, append the final range.

### 📊 Example
Input: `nums = [0,1,2,4,5,7]`

Output: `["0->2","4->5","7"]`

### ⏱️ Complexity
- Time: O(n) – Single pass through the array

- Space: O(1) – Excluding the output list

👉 See full code in [summary_ranges.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-29/summary_ranges.py)
