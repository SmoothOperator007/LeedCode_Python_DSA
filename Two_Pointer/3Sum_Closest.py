"""
Problem: 16. 3Sum Closest
Difficulty: Medium
Pattern: Two Pointers (Opposite-Direction Pointers)

Learn:
Using Sort to make it easier to access List from left and right
How the pointer movement logic works:
   - If current_sum == target, we found an exact match (return immediately).
   - If current_sum is too small, we need a larger value, so we increment `left`, as it is too small we increase the small value so we might get target.
   - If current_sum is too large, we need a smaller value, so we decrement `right`, as it is too large we decrement the large value to get near target.
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """:type nums: List[int] :type target: int :rtype: int"""
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
