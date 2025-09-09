# Problem: Design Parking System
# Link: https://leetcode.com/problems/design-parking-system/description/
# Tags: Design, Simulation
# Approach: Keep three counters for big/medium/small capacities. On addCar, check and decrement
#           the corresponding counter if available; otherwise return False.
# Time Complexity: O(1) per operation
# Space Complexity: O(1)


class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
      
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            return False
          
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            return False
          
        else:       # carType == 3
            if self.small > 0:
                self.small -= 1
                return True
            return False
