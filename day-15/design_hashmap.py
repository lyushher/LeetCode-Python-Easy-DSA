# Problem: Design HashMap
# Link: https://leetcode.com/problems/design-hashmap/description/
# Tags: Hash Map, Design, Data Structures
# Approach: Separate chaining with prime-sized bucket array; store [key, value] pairs and update in-place
# Time Complexity: Average O(1) for put/get/remove; Worst-case O(n) if all keys collide
# Space Complexity: O(n) to store key-value pairs


class MyHashMap:

    def __init__(self):
        
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
      
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
