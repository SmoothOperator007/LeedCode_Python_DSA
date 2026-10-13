"""
Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Pattern: Arrays & Hashing (Set Conversion & In-Place Slice Mutation)

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Two Pointers (In-Place Array Modification)
- Intuition: Maintain a slow pointer (`k`) for the position of unique elements and a fast pointer to scan the array, copying unique items forward in $O(1)$ space.
- Complexity: Time O(n), Space O(1).

Learning: 
1. Instant Deduplication via Set:
   - Wrapping `set(nums)` immediately drops all duplicate values out of the array.
2. Conversion & Re-sorting:
   - Since a set is unordered, we cast it back into a `list()` and call `.sort()` to restore the ascending order.
3. In-Place Container Mutation via Slices:
   - Reassigning `nums = unique_list` would only change a local variable pointer and fail LeetCode's reference checks.
   - Using slice assignment `nums[:] = unique_list` mutates the *original memory container* in-place, satisfying the custom judge.
4. Complexity:
   - Time Complexity: O(n log n) because of sorting the unique elements.
   - Space Complexity: O(n) because a new set and list are allocated in memory.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """:type nums: List[int] :rtype: int"""
        unique_list = list(set(nums))  # Step 1: Remove duplicates
        unique_list.sort()             # Step 2: Sort the elements
        nums[:] = unique_list          # Step 3: Mutate original array container
        return len(nums)
