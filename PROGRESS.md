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

**Notes:** Calculated the number of trailing zeroes in n! by counting how many times 5 appears as a factor in the numbers from 1 to n. This avoids full factorial computation and ensures logarithmic time with constant space.

Generated the n-th term of the count-and-say sequence by simulating how humans would describe digits in the previous term — grouping consecutive characters, counting them, and appending results in a loop. Practiced string construction and pattern recognition, which strengthens iterative string manipulation and edge-case handling.

---

## 📅 Day 17 – Binary Search Applications

- ✅ [Find Smallest Letter Greater Than Target](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/find_smallest_letter_greater_than_target.py)
- ✅ [Guess Number Higher or Lower](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-17/guess_number_higher_or_lower.py)

**Notes:** Applied binary search to locate the smallest letter strictly greater than a target in a sorted list. Leveraged sorted order to achieve O(log n) performance and implemented wrap-around logic to return the first element if no letter exceeded the target.

Implemented a binary search guessing strategy to find a hidden number within a range using the provided `guess()` API. Adjusted the search boundaries based on API feedback (`-1`,` 1`, or`0`), ensuring minimal guesses and logarithmic time complexity.

---

## 📅 Day 18 – Binary Search Fundamentals
- ✅ [Search Insert Position](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-18/search_insert_position.py)
- ✅ [First Bad Version](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-18/first_bad_version.py)

**Notes:** Combined two fundamental binary search patterns — first, locating either the exact target index or its correct insertion point in a sorted array by adjusting left and right boundaries until convergence, ensuring that the final `left` pointer provides the insertion index without extra passes; second, pinpointing the earliest bad version in a sequence by integrating the `isBadVersion()` API into the search loop, recording each bad mid as a candidate and narrowing the range toward the earliest occurrence — both solutions halving the search space at each step to achieve optimal O(log n) time with constant O(1) space usage.

---

## 📅 Day 19 – Integer Roots & Perfect Squares
- ✅ [Sqrt(x)](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-19/sqrt_x.py)
- ✅ [Valid Perfect Square](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-19/valid_perfect_square.py)

**Notes:**
Practiced two fundamental problems around square roots using binary search. In the first, calculated the integer square root by repeatedly narrowing the range until finding the largest mid whose square is less than or equal to `x`, ensuring the result is the floor of the true square root. In the second, verified whether a number is a perfect square by testing midpoints in the search range and checking if any squared value equals the input, guaranteeing logarithmic runtime without using built-in math functions.

## 📅 Day 20 – Bit Manipulation Basics
- ✅ [Power of Two](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-20/power_of_two.py)
- ✅ [Number of 1 Bits](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-20/number_of_1_bits.py)

**Notes:**
Explored two classic bit manipulation problems. In the first, verified whether a number is a power of two by leveraging the property that such numbers have exactly one set bit in their binary representation, using the condition `n > 0` and `n & (n - 1) == 0` for a constant-time check. In the second, counted the number of set bits in an integer by applying Brian Kernighan’s algorithm, repeatedly clearing the lowest set bit with `n & (n - 1)` and incrementing a counter, which ensures efficient O(k) runtime where k is the number of 1-bits. Both problems highlight how bitwise operations provide elegant, high-performance solutions to fundamental questions.

---

## 📅 Day 21 – Tree Depth & Structural Equality

- ✅ [Maximum Depth of Binary Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-21/maximum_depth_of_binary_tree.py)
- ✅ [Same Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-21/same_tree.py)

**Notes:**
Worked on two fundamental binary tree problems. In the first, computed the maximum depth of a binary tree by recursively exploring both subtrees and returning `1 + max(left, right)`, ensuring every node is visited exactly once and the longest path from root to leaf is measured. In the second, determined whether two trees are identical by recursively comparing node values and structure in parallel, confirming equality only when both subtrees matched completely. These problems reinforce core DFS recursion patterns on trees, emphasizing structural traversal and balanced handling of base cases.

---

## 📅 Day 22 – Binary Tree Symmetry & Inversion
- ✅ [Symmetric Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-22/symmetric_tree.py)
- ✅ [Invert Binary Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-22/invert_binary_tree.py#)

**Notes:** Focused on structural transformations of binary trees. In the first problem, checked whether a binary tree is symmetric by recursively comparing mirrored node pairs from the left and right subtrees, ensuring both values and structures matched in a mirror-like fashion. In the second, inverted the binary tree by recursively swapping the left and right children of each node, propagating local changes into a complete tree-wide transformation. Together, these problems emphasize recursive divide-and-conquer strategies, mirrored traversals, and how small, consistent operations applied at each node can globally reshape a tree.

---

## 📅 Day 23 – Tree Path & Balance Checks
- ✅ [Path Sum](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-23/path_sum.py)
- ✅ [Balanced Binary Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-23/balanced_binary_tree.py)

**Notes:** Tackled two classic DFS-based binary tree problems. In the first, determined whether a root-to-leaf path exists that sums to a given target by recursively subtracting node values and checking at leaves if the remaining sum matches — ensuring every potential path is explored. In the second, verified if a binary tree is height-balanced by combining height calculation with balance checks in a single bottom-up traversal; each node contributes `1 + max(left, right)` if balanced, or fails early when imbalance is detected. Both problems highlight the efficiency of recursion in handling cumulative path constraints and structural validation with linear O(n) traversal.

---

## 📅 Day 24 – Binary Tree Depth & Range Sum
- ✅ [Minimum Depth of Binary Tree](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-24/minimum_depth_of_binary_tree.py)
- ✅ [Range Sum of BST](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-24/range_sum_of_bst.py)

**Notes:** Practiced two BST-focused problems that emphasize recursion and pruning. In the first, computed the minimum depth of a binary tree by carefully handling cases where one child is null, ensuring that only true leaf paths are counted. This avoids incorrectly returning zero for incomplete subtrees. In the second, optimized the sum of node values within a given range by leveraging the BST property to prune unnecessary branches: skipping the left subtree if the node value is too small, or the right if it’s too large. Both problems highlight efficient recursive traversal strategies that reduce unnecessary computation while maintaining clarity and correctness.

---

## 📅 Day 25 – Complete Trees & Leaf Sequences
- ✅ [Count Complete Tree Nodes](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-25/count_complete_tree_nodes.py)
- ✅ [Leaf-Similar Trees](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-25/leaf_similar_trees.py)

**Notes:** Counted nodes in a complete binary tree without traversing every node by comparing left/right subtree heights; when heights match, the left subtree is a perfect tree contributing 2^h − 1 nodes and we recurse on the right, otherwise the right is perfect and we recurse on the left—yielding an efficient divide-and-conquer solution with O((log n)²) time and O(log n) space. Then verified leaf similarity of two trees by performing DFS to extract the left-to-right leaf sequences and comparing them for equality, emphasizing order and values while ignoring internal structure; this runs in O(n + m) time with O(h₁ + h₂) stack usage.

---

## 📅 Day 26 – Array Manipulation & Missing Numbers
- ✅ [Move Zeroes](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-26/move_zeroes.py)
- ✅ [Find All Numbers Disappeared in an Array](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-26/find_all_numbers_disappeared_in_an_array.py)
 
**Notes:** Focused on in-place array manipulation techniques. In the first problem, efficiently pushed all zeroes to the end while preserving the order of non-zero elements using a two-pointer approach that overwrites non-zero values forward and fills the rest with zeros, achieving O(n) time and O(1) space. In the second, identified all missing numbers in the range [1, n] by marking visited indices via sign flipping, then collecting positions that remained positive as the missing values. Both problems reinforced the use of index-based logic and in-place modifications to optimize space while keeping solutions linear in time.

---

## 📅 Day 27 – Ranking & Character Difference
- ✅ [Relative Ranks](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-27/relative_ranks.py)
- ✅ [Find the Difference](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-27/find_the_difference.py)

**Notes:** Solved two array and string-based problems. In the first, assigned medals and ranks by pairing scores with original indices, sorting in descending order, and mapping top performers to medals while giving numeric ranks to the rest, ensuring results were restored to the input order. In the second, detected the extra character between two strings by applying XOR across all characters, leveraging the property that identical values cancel out and leaving only the added character. Both problems highlight efficient use of sorting, indexing, and bitwise operations to reduce time and space complexity.

---

## 📅 Day 28 – String Prefix & Keyboard Row
- ✅ [Longest Common Prefix](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-28/longest_common_prefix.py)
- ✅ [Keyboard Row](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-28/keyboard_row.py)

**Notes:** Focused on string scanning and set-based filtering. For the first problem, derived the longest shared prefix by comparing the first word character-by-character against all others and stopping at the earliest mismatch, enabling early termination with O(S) time and O(1) space. For the second, modeled each keyboard row as a fixed set and tested whether each word’s character set was a subset of any row, returning only those typable from a single row; this keeps the solution simple and fast with O(n·k) time and constant extra space.

---

## 📅 Day 29 – Substrings & Range Summaries
- ✅ [Longest Substring Without Repeating Characters](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-29/longest_substring_without_repeating_characters.py)
- ✅ [Summary Ranges](https://github.com/lyushher/LeetCode-Python-Easy-DSA/blob/main/day-29/summary_ranges.py)

**Notes:** Practiced sliding window and range summarization techniques. In the first problem, maintained a dynamic window with two pointers and a hash map of last seen indices to efficiently handle duplicates, ensuring each substring remained unique and updating the maximum length in O(n) time. In the second, summarized consecutive integer ranges by tracking the start of each segment and recording either a single number or a "start->end" range whenever continuity broke, finishing with the final segment. These problems reinforced mastery of sliding windows, index tracking, and array scanning patterns.
