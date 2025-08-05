# Day - 07
## ⭐️ Reverse String – 7.1
### 🔗 Problem
[LeetCode #344 – Reverse String](https://leetcode.com/problems/reverse-string/)

### 🧠 Core Idea
Use two pointers to reverse the string by swapping characters from both ends.
The algorithm performs all swaps in-place and avoids extra space usage.
This is a classic technique for array/string manipulation using minimal memory.

### 📊 Example
Input: s = ["h","e","l","l","o"]

Output: ["o","l","l","e","h"]

### ⏱️ Complexity
Time: O(n) – Each character is visited once

Space: O(1) – In-place with constant memory

👉 See full code in [reverse_string.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-07/reverse_string.py)

## ⭐️ First Unique Character in a String – 7.2
### 🔗 Problem
[LeetCode #387 – First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

### 🧠 Core Idea
Use a hash map to count how many times each character appears in the string.
Then iterate through the original string to find the first character with a frequency of one.
This approach ensures the correct index is returned with a single scan after counting.

### 📊 Example
Input: s = "leetcode"

Output: 0 → Because 'l' is the first character that appears only once

### ⏱️ Complexity
Time: O(n) – One pass to count, one pass to scan

Space: O(1) – Max 26 lowercase characters

👉 See full code in [first_unique_character.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-07/first_unique_character_in_a_string.py)

