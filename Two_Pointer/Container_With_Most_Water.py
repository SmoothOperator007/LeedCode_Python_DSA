"""
Problem: 11. Container With Most Water
Difficulty: Medium
Pattern: Two Pointers (Opposite-Direction Pointers)

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Two Pointers (Opposite-Direction Pointers) + Greedy Strategy
- Intuition: Place pointers at both ends of the container. The water area is limited by the shorter line and the distance between them. To maximize area, greedily move the pointer pointing to the shorter line inward in hopes of finding a taller line.
- Complexity: Time O(n), Space O(1).

Learn:-
1. Why Opposite-Direction Pointers work:
   - We place one pointer at the extreme left and one at the extreme right of the array.
   - The area of water is determined by the *shorter* vertical line and the *distance* between the pointers.
2. How to decide which pointer to move:
   - width is the distance of the 2 pointers, starting from their extremes sides, current_height using min and max_water comparing the area to the
     current area we are find to the max_area we get which will be retained.
   - Main is the conditional where we shift our pointers based on which side of pointer is shorter, i.e we move the pointer that is shorter as the we need 
     the max area for which we need max height so we shift the shortest pointer out of the 2 to get the max area, and like this we loop through the whole
     list.
3. Complexity:
   - Time Complexity: O(n) because each element is visited at most once as the pointers move inward.
   - Space Complexity: O(1) auxiliary space since we only use two pointers and a max variable.
"""

class Solution(object):
    def maxArea(self, height):
        """:type height: List[int] :rtype: int"""
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width between the two lines
            width = right - left
            # Height is constrained by the shorter line
            current_height = min(height[left], height[right])
            # Calculate current area and update maximum
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Greedily move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
