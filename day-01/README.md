# Day - 01

## ⭐️ Two Sum - 1.1

### 🔗 Problem
[LeetCode #1 – Two Sum](https://leetcode.com/problems/two-sum/)

### 🧠 Core Idea  
Check every pair of numbers to find two that sum to the target.  
Brute-force approach — simple, direct, no optimization.

### 📊 Example  
Input: `nums = [2, 7, 11, 15]`, `target = 9`  
Output: `[0, 1]` → Because `2 + 7 = 9`

### ⏱️ Complexity  
- **Time:** O(n²)  
- **Space:** O(1)

👉 See full code in [`two_sum.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-01/two_sum.py)

---

## ⭐️ Best Time to Buy and Sell Stock - 1.2

### 🔗 Problem  
[LeetCode #121 – Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### 🧠 Core Idea  
Track the **lowest price so far** while iterating through the list.  
At each step, calculate the potential profit if sold today and update the **max profit** when it's higher.  
Greedy approach – one pass.

### 📊 Example  
Input: `prices = [7, 1, 5, 3, 6, 4]`  
Output: `5` → Buy at `1`, sell at `6`.

### ⏱️ Complexity  
- **Time:** O(n) – Single pass through prices  
- **Space:** O(1) – Only two variables used  

👉 See full code in [`best_time_to_buy_and_sell_stock.py`](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-01/best_time_to_buy_and_sell_stock.py)
