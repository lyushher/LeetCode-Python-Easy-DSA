# Problem: Design Linked List
# Link: https://leetcode.com/problems/design-linked-list/description/
# Tags: Linked List, Design, Doubly Linked List
# Approach: Implemented a doubly linked list using sentinel head and tail nodes to simplify insertions and deletions.
# Time Complexity:
#   - get: O(min(index, n - index)) by traversing from the closer end
#   - addAtHead / addAtTail: O(1)
#   - addAtIndex / deleteAtIndex: O(min(index, n - index))
# Space Complexity: O(n) for storing all nodes


class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _getNode(self, index):
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr

    def _addBetween(self, prev, nxt, val):
        node = Node(val)
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node
        self.size += 1

    def _removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        return self._getNode(index).val

    def addAtHead(self, val):
        self._addBetween(self.head, self.head.next, val)

    def addAtTail(self, val):
        self._addBetween(self.tail.prev, self.tail, val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            target = self._getNode(index)
            self._addBetween(target.prev, target, val)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        target = self._getNode(index)
        self._removeNode(target)
