# LeetCode Easy Problems – 30-Day Python Progress Tracker

> A structured daily log of LeetCode easy problems solved in Python, focused on building strong data structure and algorithms fundamentals for top-tier technical interviews.

---

## 📅 Day 1 – Arrays & Brute Force

- ✅ [Two Sum](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-01/two_sum.py)  
- ✅ [Best Time to Buy and Sell Stock](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-01/best_time_to_buy_and_sell_stock.py) 

**Notes:** Practiced brute force and greedy techniques. Focused on understanding nested iteration and real-time min tracking.

---

## 📅 Day 2 – Arrays & Hashing Fundamentals

- ✅ [Contains Duplicate](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-02/contains_duplicate.py)
- ✅ [Valid Anagran](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-02/valid_anagram.py)

**Notes:** Applied hashing strategies to detect duplicates and analyze character distributions in strings.
Focused on optimizing search and comparison operations using constant-time lookups with sets and dictionaries.

---

## 📅 Day 3 - Hash Maps & Voting Algorithm

- ✅ [Intersection of Two Arrays II](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-03/intersection_of_two_arrays_2.py)
- ✅ [Majority Element](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-03/majority_element.py)

**Notes:** Utilized hash maps to solve array intersection problems with duplicate tracking.  
Applied Boyer–Moore Voting to optimize majority element detection to O(1) space — a core interview pattern.

---

## 📅 Day 4 – Bit Manipulation Patterns
- ✅ [Single Number](https://leetcode.com/problems/single-number/description/)
- ✅ [Missing Number](https://leetcode.com/problems/missing-number/)

**Notes:** Explored XOR-based logic to isolate non-duplicate values and determine missing elements efficiently.
Applied bit-level identities like `a ^ a = 0` to reduce problems into linear-time, constant-space operations.

---

## 📅 Day 5 – In-Place Algorithms & Simulation Logic
- ✅ [Merge Sorted Array](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-05/merged_sorted_array.py)
- ✅ [Plus One](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-05/plus_one.py)

**Notes:** Focused on in-place merging by shifting from the back to preserve original values during overwrite.
Handled number incrementation digit by digit, managing carry propagation without relying on conversions.

---

## 📅 Day 6 – String Filtering & Substring Matching
- ✅ [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- ✅ [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

**Notes:** Cleaned and normalized string inputs to handle case and symbol inconsistencies.
Used a sliding window approach to locate substrings, reinforcing logic used in low-level pattern matching problems.

---

## 📅 Day 7 – Two-Pointer Reversal & Frequency Filtering
- ✅ [Reverse String](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-07/reverse_string.py)
- ✅ [First Unique Character in a String](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-07/first_unique_character_in_a_string.py)

**Notes:** Reversed strings in-place using the two-pointer technique, avoiding additional memory usage.
Counted character frequencies to identify the first non-repeating character — a common pattern in real-world text parsing and filtering tasks.

---

## 📅 Day 8 – Stack Validation & In-Place Deduplication
- ✅ [Valid Parentheses](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-08/valid_parentheses.py)
- ✅ [Remove Duplicates from Sorted Array](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-08/remove_duplicates_from_sorted_array.py)

**Notes:** Used a stack to validate proper matching and nesting of parentheses — a common pattern in syntax checking and expression parsing.
Employed a two-pointer strategy to remove duplicates in sorted arrays without extra space, reinforcing in-place overwrite techniques.

---

## 📅 Day 9 – Stack-Based Data Structure Design
- ✅ [Implement Queue using Stacks](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-09/implement_queue_using_stacks.py)
- ✅ [Min Stack](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-09/min_stack.py)

**Notes:** Designed queue and stack variations using only stack operations, focusing on O(1) amortized performance.
Implemented a queue with two stacks for efficient enqueue and dequeue, and a stack that tracks the minimum element in constant time via an auxiliary stack.

---

## 📅 Day 10 – String Parsing & Linear Scans
- ✅ [Roman to Integer](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-10/roman_to_integer.py)
- ✅ [Length of Last Word](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-10/length_of_last_word.py)

**Notes:** Strengthened string processing skills through two distinct linear-scan problems.
Applied right-to-left traversal with conditional subtraction to accurately convert Roman numerals.
Used trimming and reverse scanning to compute the final word length without additional data structures, ensuring both solutions remain optimal and memory-efficient.

---

## 📅 Day 11 – Linked List Rewiring & Merging
- ✅ [Reverse Linked List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-11/reverse_linked_list.py)
- ✅ [Merge Two Sorted Lists](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-11/merge_two_sorted_lists.py)

**Notes:** Reversed pointers iteratively to flip a singly linked list in-place with constant extra space.
Merged two sorted lists using a dummy head and tail pointer, attaching the smaller node each step to build a single sorted list efficiently.

---

## 📅 Day 12 – Linked List Cycle Detection & Palindrome Check
- ✅ [Linked List Cycle](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-12/linked_list_cycle.py)
- ✅ [Palindrome Linked List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-12/palindrome_linked_list.py)

**Notes:** Detected cycles in a linked list using Floyd’s Tortoise and Hare algorithm, achieving O(1) space without modifying the list.
Checked if a linked list is a palindrome by finding the middle, reversing the second half in-place, and comparing both halves — an efficient approach that avoids extra space.

---

## 📅 Day 13 – Linked List Deletion & Deduplication
- ✅ [Delete Node in a Linked List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-13/delete_node_in_a_linked_list.py)
- ✅ [Remove Duplicates from Sorted List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-13/remove_duplicates_from_sorted_list.py)

**Notes:** Removed a node without head access by copying data from the next node and bypassing it — a constant-time, in-place deletion trick.
Eliminated consecutive duplicates in a sorted linked list with a single traversal, adjusting pointers to maintain sorted order and ensure all elements are unique without extra space.

---

## 📅 Day 14 – Linked List Midpoint & Intersection Detection
- ✅ [Middle of the Linked List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-14/middle_of_the_linked_list.py)
- ✅ [Intersection of Two Linked Lists](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-14/intersection_of_two_linked_lists.py)

**Notes:** Found the middle of a linked list using the fast and slow pointer method, ensuring O(1) space and correctly returning the second middle node when the list length is even.
Detected the intersection node of two linked lists with the two-pointer switching technique, guaranteeing both pointers traverse equal total distances without extra memory, achieving optimal O(n + m) time and O(1) space complexity.

---

## 📅 Day 15 – Custom Data Structure Design
- ✅ [Design Linked List](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-15/design_linked_list.py)
- ✅ [Design HashMap](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-15/design_hashmap.py)

**Notes:** Built a fully functional singly linked list supporting index-based retrieval, insertion, and deletion, with O(1) head/tail updates and size tracking for constant-time boundary checks.
Implemented a hash map using separate chaining with a prime-sized bucket array for improved key distribution. Achieved O(1) average-case put, get, and remove operations, while gracefully handling collisions via linked lists — noting that worst-case performance can degrade to O(n) if many keys hash to the same bucket.

---

## 📅 Day 16 – Math Foundations & Basic Looping

- ✅ [Factorial Trailing Zeroes](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-16/fibonacci_number.py)

- ✅ [Count and Say](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-16/binary_search.py)

**Notes:**
Calculated the number of trailing zeroes in n! by counting how many times 5 appears as a factor in the numbers from 1 to n. This avoids full factorial computation and ensures logarithmic time with constant space.

Generated the n-th term of the count-and-say sequence by simulating how humans would describe digits in the previous term — grouping consecutive characters, counting them, and appending results in a loop. Practiced string construction and pattern recognition, which strengthens iterative string manipulation and edge-case handling.

---

## 📅 Day 17 – Binary Search Applications

- ✅ [Find Smallest Letter Greater Than Target](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/find_smallest_letter_greater_than_target.py)
- ✅ [Guess Number Higher or Lower](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/guess_number_higher_or_lower.py)

**Notes:**
Applied binary search to locate the smallest letter strictly greater than a target in a sorted list. Leveraged sorted order to achieve O(log n) performance and implemented wrap-around logic to return the first element if no letter exceeded the target.

Implemented a binary search guessing strategy to find a hidden number within a range using the provided `guess()` API. Adjusted the search boundaries based on API feedback (`-1`,` 1`, or`0`), ensuring minimal guesses and logarithmic time complexity.


