# Day - 09
## ⭐️ Implement Queue using Stacks – 9.1
### 🔗 Problem
[LeetCode #232 – Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### 🧠 Core Idea
Simulate a queue using two stacks: one for incoming elements and one for outgoing elements.
When dequeuing or peeking, transfer elements from the incoming stack to the outgoing stack only if the outgoing stack is empty.
This lazy transfer ensures amortized O(1) time complexity for queue operations.

### 📊 Example
Input: ["MyQueue","push","push","peek","pop","empty"], [[],[1],[2],[],[],[]]

Output: [null,null,null,1,1,false]

### ⏱️ Complexity
Time: O(1) amortized for each operation

Space: O(n) – Combined storage in both stacks

👉 See full code in [implement_queue_using_stacks.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-09/implement_queue_using_stacks.py)

## ⭐️ Min Stack – 9.2
### 🔗 Problem
[LeetCode #155 – Min Stack](https://leetcode.com/problems/min-stack/)

### 🧠 Core Idea
Maintain two stacks: one for storing values and one for tracking the minimum at each push.
When pushing, also push the smaller value between the new element and the previous minimum to the min stack.
This allows retrieving the minimum in O(1) time without scanning the entire stack.

### 📊 Example
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]

Output: [null,null,null,null,-3,null,0,-2]

### ⏱️ Complexity
Time: O(1) for all operations

Space: O(n) – Values stored in two stacks

👉 See full code in [min_stack.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-09/min_stack.py)
