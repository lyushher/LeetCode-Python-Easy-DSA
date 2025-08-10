# Problem: Delete Node in a Linked List
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Tags: Linked List, In-Place, O(1)
# Approach: Copy the value of the next node into the current node, then bypass the next node
# Time Complexity: O(1) – Constant time since no traversal is needed
# Space Complexity: O(1) – No extra data structures


# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val  # copy the value from the next node into the current node
        
        node.next = node.next.next    # skip the next node by pointing to the node after it
