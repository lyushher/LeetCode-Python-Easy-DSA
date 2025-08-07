# Day - 10
## ⭐️ Roman to Integer – 10.1
### 🔗 Problem
[LeetCode #13 – Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

### 🧠 Core Idea
Map Roman numerals to their integer values and process the string from right to left.
Add values normally, but subtract when a smaller numeral precedes a larger one to handle cases like IV or IX.
This ensures accurate conversion in a single pass with constant space.

### 📊 Example
Input: s = "MCMXCIV"

Output: 1994 → Because M(1000) + CM(900) + XC(90) + IV(4) = 1994

### ⏱️ Complexity
Time: O(n) – One pass through the string

Space: O(1) – Constant extra space

👉 See full code in [roman_to_integer.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-10/roman_to_integer.py)

## ⭐️ Length of Last Word – 10.2
### 🔗 Problem
[LeetCode #58 – Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

### 🧠 Core Idea
Trim spaces from both ends of the string and split it into words.
The last word in the list is the final word in the original string.
Return its length as the result.

### 📊 Example
Input: s = "Hello World"

Output: 5 → Because the last word "World" has 5 letters

### ⏱️ Complexity
Time: O(n) – Traverses the string once for trimming and splitting

Space: O(n) – Due to storing the word list

👉 See full code in [length_of_last_word.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-10/length_of_last_word.py)
