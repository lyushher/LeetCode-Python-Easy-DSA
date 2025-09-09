# Day 30 

## ⭐️ Design Parking System – 30.1
### 🔗 Problem
[LeetCode #1603 – Design Parking System](https://leetcode.com/problems/design-parking-system/)

### 🧠 Core Idea
Maintain three counters for big, medium, and small slots.
On each addCar call, check the counter for the requested type: if greater than zero, decrement and return True; otherwise return False.
This ensures O(1) operations with constant memory.

### 📊 Example
Input: ["ParkingSystem","addCar","addCar","addCar","addCar"], [[1,1,0],[1],[2],[3],[1]]

Output: [null,true,true,false,false]

### ⏱️ Complexity
- Time: O(1) per operation

- Space: O(1)

👉 See full code in [design_parking_system.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-30/design_parking_system.py)

---

## ⭐️ Reverse Words in a String III – 30.2
### 🔗 Problem
[LeetCode #557 – Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

### 🧠 Core Idea
Split the input string by spaces, reverse each word individually, and then rejoin with spaces. This keeps the word order intact but reverses characters within each word.

### 📊 Example
Input: s = "Let's take LeetCode contest"

Output: "s'teL ekat edoCteeL tsetnoc"

### ⏱️ Complexity
- Time: O(n) – n is the total number of characters

- Space: O(n) – for the output string

👉 See full code in [reverse_words_in_a_string_iii.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-30/reverse_words_in_a_string_iii.py)
