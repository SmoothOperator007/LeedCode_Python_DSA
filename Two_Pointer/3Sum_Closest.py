"""
Problem: 16. 3Sum Closest
Difficulty: Medium
Pattern: Two Pointers (Opposite-Direction Pointers)

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Two Pointers (Opposite-Direction Pointers) + Sorting
- Intuition: Sort the array to enable efficient scanning. Fix one number and use two pointers (left and right) moving inward based on whether the current triplet sum is smaller or larger than the target, updating the closest sum along the way.
- Complexity: Time O(n^2), Space O(1).

Learning:
1. Using Sort: 
   - Sorting makes it much easier to access and scan the list from left and right systematically.
2. How the pointer movement logic works:
   - If current_sum == target, we found an exact match (return immediately).
   - If current_sum is too small, we need a larger value, so we increment `left`. 
     (Since the sum is too small, increasing the smaller value pulls us closer to the target).
   - If current_sum is too large, we need a smaller value, so we decrement `right`. 
     (Since the sum is too large, decrementing the larger value pulls us closer to the target).
3. Complexity:
   - Time Complexity: O(n^2) due to the outer loop and the inner two-pointer scan.
   - Space Complexity: O(1) auxiliary space.
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
