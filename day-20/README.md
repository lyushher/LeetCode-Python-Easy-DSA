# Day - 20
## ⭐️ Power of Two – 20.1
### 🔗 Problem

[LeetCode #231 – Power of Two](https://leetcode.com/problems/power-of-two/)

### 🧠 Core Idea

A number is a power of two if it has only one bit set in its binary form.
Check positivity (n > 0) and then apply the bitwise trick: n & (n - 1) == 0.
This clears the lowest set bit; if the result becomes 0, the number had only one set bit → it’s a power of two.

### 📊 Example

Input: n = 16 -> Output: true (binary 10000)

Input: n = 3 -> Output: false (binary 11)

### ⏱️ Complexity

- Time: O(1) – Single bitwise operation

- Space: O(1) – No extra memory

👉 See full code in [power_of_two.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-20/power_of_two.py)

---

## ⭐️ Number of 1 Bits – 20.2
### 🔗 Problem

[LeetCode #191 – Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

### 🧠 Core Idea

The Hamming Weight of an integer can be counted using Brian Kernighan’s Algorithm.
Each time we apply n = n & (n - 1), the lowest set bit is removed.
The number of iterations until n becomes 0 equals the number of 1-bits in the binary representation.

### 📊 Example

Input: n = 11 (binary 1011) -> Output: 3

Input: n = 128 (binary 10000000) -> Output: 1

### ⏱️ Complexity

- Time: O(k) where k is the number of set bits (worst-case O(32))

- Space: O(1) – Only a counter variable

👉 See full code in [number_of_1_bits.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-20/number_of_1_bits.py)
