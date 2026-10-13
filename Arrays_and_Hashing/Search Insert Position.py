"""
Problem: Search Insert Position
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Binary Search
- Intuition: Because the array is sorted, we can use binary search to locate the target or find the exact insertion index where `nums[left] >= target`. 
- Time Complexity: O(log n) because the search space is halved in each iteration.
- Space Complexity: O(1) auxiliary space.

--- LEARNING ---
- Custom Intuition: Your initial approach combined membership checking (`target in nums`) with a linear search to find insertion points. While clever and effective for passing small test cases in 0 ms, it checks the array multiple times, resulting in O(n) linear time complexity.
- Trade-offs: Transitioning from a linear scan to Binary Search brings the time complexity down to logarithmic scale, which is essential when handling very large sorted arrays in interviews.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # If not found, `left` points to the correct insertion index
        return left


"""Another easy way was"""

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            # If we find the target or an element greater than the target, 
            # this index is our answer.
            if nums[i] >= target:
                return i
        
        # If we loop through everything and the target is larger than all elements,
        # it belongs at the very end.
        return len(nums)

"""or"""

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            # If we find the target or an element greater than the target, 
            # this index is our answer.
            if nums[i] >= target:
                return i
            else:
              return len(nums)
