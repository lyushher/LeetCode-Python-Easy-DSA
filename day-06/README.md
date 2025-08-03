# Day - 06
## ⭐️ Valid Palindrome – 6.1
### 🔗 Problem
[LeetCode #125 – Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### 🧠 Core Idea
Clean the input string by removing all non-alphanumeric characters and converting it to lowercase.
Then use two pointers to check if the cleaned string reads the same forwards and backwards.
This approach handles edge cases like punctuation and mixed casing efficiently.

### 📊 Example
Input: s = "A man, a plan, a canal: Panama"

Output: true → Because after cleaning it becomes "amanaplanacanalpanama"

### ⏱️ Complexity
Time: O(n) – One pass to filter and one to compare

Space: O(n) – Due to the cleaned string

👉 See full code in [valid_palindrome.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-06/valid_palindrome.py)

## ⭐️ Find the Index of the First Occurrence in a String – 6.2
### 🔗 Problem
[LeetCode #28 – Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

### 🧠 Core Idea
Slide a window of the same length as the needle over the haystack.
At each position, compare the current substring with the needle.
Return the first matching index, or -1 if no match is found.

### 📊 Example
Input: haystack = "sadbutsad", needle = "sad"

Output: 0 → Because the first "sad" appears at index 0

### ⏱️ Complexity
Time: O(n * m) – Worst-case with nested comparison

Space: O(1) – No extra space used

👉 See full code in [find_index_first_occurrence.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-06/find_index_first_occurrence.py)
