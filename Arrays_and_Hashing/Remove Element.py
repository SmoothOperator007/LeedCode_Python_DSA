"""
Problem: Remove Element (LeetCode)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two Pointers (In-place Array Modification)
Intuition: 
Interviewers and optimal standards look for an O(N) time solution that minimizesunnecessary shifts. 
By maintaining a placement index (`k`), we iterate through the array once, copying non-target elements to the front. 
This avoids the quadratic time complexity caused by repeatedly shifting elements during deletions.
Time Complexity: O(N) where N is the number of elements in nums.
Space Complexity: O(1) as modifications are done entirely in-place.

--- LEARNING ---
My Custom Intuition & Logic:
- Instead of complex pointer manipulation, I utilized a `while` loop combined   with Python's built-in `.remove()` method (`while val in nums: nums.remove(val)`).
- This approach continuously scans and pops out all target values until none remain.
- Complexity Trade-off: While `.remove()` causes an internal O(N) shift per deletion 
  (leading to a theoretical worst-case time complexity of O(N^2)), the practical execution 
  speed for typical constraints is exceptionally fast (0 ms), showcasing a clean balance 
  between code readability and performance.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        
        return len(nums)


######################################################
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

#This is Classic 2 pointer method

"""
Here is how the two pointers break down in your code:

The Fast Pointer (i): Driven by range(len(nums)), this pointer moves rapidly through every single element of the array one by one to inspect them.

The Slow / Write Pointer (k): This pointer moves strictly at its own pace, only advancing when it finds a valid element that needs to be kept.
It marks the exact boundary where the next valid element should be written.
"""
