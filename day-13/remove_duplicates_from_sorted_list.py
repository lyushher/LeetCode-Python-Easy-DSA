# Problem: Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Tags: Linked List, Two-Pointer
# Approach: Traverse the list, skipping nodes with duplicate values
# Time Complexity: O(n) – Single pass through the list
# Space Complexity: O(1) – In-place modification without extra data structures


# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        # traverse while there is a next node
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip the duplicate node
              
            else:
                current = current.next  # move to the next node if no duplicate
        
        return head
