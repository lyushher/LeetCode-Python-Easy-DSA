# Day - 14
## ⭐️ Middle of the Linked List – 14.1
### 🔗 Problem
[LeetCode #876 – Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

### 🧠 Core Idea
Use the fast and slow pointer approach:
The slow pointer moves one step at a time, while the fast pointer moves two steps.
When the fast pointer reaches the end, the slow pointer will be at the middle.
If there are two middle nodes, this method naturally returns the second one as required.

### 📊 Example
Input: head = [1,2,3,4,5]

Output: [3,4,5] → The middle node is 3

### ⏱️ Complexity
- Time: O(n) – Single traversal of the list

- Space: O(1) – No extra memory used

👉 See full code in [middle_of_linked_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-14/middle_of_the_linked_list.py)

---

## ⭐️ Intersection of Two Linked Lists – 14.2
### 🔗 Problem
[LeetCode #160 – Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

### 🧠 Core Idea
Apply the two-pointer switching technique:
Traverse both lists with two pointers.
When one pointer reaches the end, redirect it to the head of the other list.
This ensures both pointers travel the same total distance and meet at the intersection node, or both reach None if no intersection exists.

### 📊 Example
Input:
headA = [4,1,8,4,5]
headB = [5,6,1,8,4,5]

Output: Reference to node with value 8

### ⏱️ Complexity
- Time: O(n + m) – At most two traversals of each list

- Space: O(1) – No additional data structures

👉 See full code in [intersection_of_two_linked_lists.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-14/intersection_of_two_linked_lists.py)
