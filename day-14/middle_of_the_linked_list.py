# Problem: Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
# Tags: Linked List, Two-Pointer
# Approach: Fast/slow pointers; when fast hits the end, slow is at the middle (returns second middle for even length)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next 
        return slow                 

