# Day - 15
## ⭐️ Design Linked List – 15.1
### 🔗 Problem

[LeetCode #707 – Design Linked List](https://leetcode.com/problems/design-linked-list/)

### 🧠 Core Idea

Implemented a singly linked list supporting index-based access, insertion at head/tail, insertion at a specific index, and deletion.
Maintained a size counter for fast index validation and performed O(1) updates for head and tail operations.

### 📊 Example

addAtHead(1) → addAtTail(3) → addAtIndex(1, 2) results in 1→2→3.
get(1) returns 2.
deleteAtIndex(1) updates list to 1→3, and get(1) returns 3.

### ⏱️ Complexity

- Time: O(n) for get, addAtIndex, deleteAtIndex; O(1) for addAtHead, addAtTail

- Space: O(1) – Only node pointers stored

👉 See full code in [design_linked_list.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-15/design_linked_list.py)

---

## ⭐️ Design HashMap – 15.2
### 🔗 Problem

[LeetCode #706 – Design HashMap](https://leetcode.com/problems/design-hashmap/)

### 🧠 Core Idea

Built a hash map using separate chaining to resolve collisions, with each bucket storing a linked list of key-value pairs.
Used a fixed-size bucket array with a prime length for better key distribution, achieving O(1) average-case performance.

### 📊 Example

put(1, 1), put(2, 2), get(1) → 1.
get(3) → -1 (not found).
put(2, 1) updates key 2’s value.
remove(2) deletes key 2, and get(2) → -1.

### ⏱️ Complexity

- Time: O(1) average for put, get, remove (O(n) worst-case if all keys collide)

- Space: O(n) – For storing key-value pairs

👉 See full code in [design_hashmap.py](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-15/design_hashmap.py)
