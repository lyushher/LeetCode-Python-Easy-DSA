# Day - 02

## ⭐️ Contains Duplicate - 2.1

### 🔗 Problem  
[LeetCode #217 – Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

### 🧠 Core Idea  
Use a **hash set** to track seen numbers.  
As you iterate through the array, check if the current number has already been seen.  
If yes → return `True`.  
If loop completes → return `False`.  
Efficient lookup using hashing.

### 📊 Example  
Input: `nums = [1, 2, 3, 1]`  
Output: `True` → Because `1` appears twice

### ⏱️ Complexity  
- **Time:** O(n) – Each element is checked and added once  
- **Space:** O(n) – In worst case, all elements are stored in the set  

👉 See full code in [`contains_duplicate.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-02/contains_duplicate.py)

---

## ⭐️ Valid Anagram - 2.2

### 🔗 Problem  
[LeetCode #242 – Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

### 🧠 Core Idea  
Use a **hash map (dictionary)** to count character frequencies in the first string,  
then subtract character counts based on the second string.  
If all frequencies balance to zero, it's a valid anagram.

### 📊 Example  
Input: `s = "anagram"`, `t = "nagaram"`  
Output: `True` → Both strings have the same character counts

### ⏱️ Complexity  
- **Time:** O(n) – One pass for counting, one pass for checking  
- **Space:** O(n) – Hash map for character frequency  

👉 See full code in [`valid_anagram.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-02/valid_anagram.py)
