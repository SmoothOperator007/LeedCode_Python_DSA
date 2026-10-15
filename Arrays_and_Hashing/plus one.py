"""
Problem: 66. Plus One
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Right-to-Left Array Iteration / Carry Propagation
Intuition: 
Traverse the array from the least significant digit (rightmost) to the most significant digit (lefttmost). 
If a digit is less than 9, increment it by 1 and immediately return the array. If it is 9, set it to 0 
and let the loop carry the addition to the next left digit. If all digits were 9, prepend a 1 at the beginning.

Time Complexity: O(N) where N is the number of digits in the array.
Space Complexity: O(1) auxiliary space (or O(N) if we must return a new array when all digits are 9).

--- LEARNING ---
My Custom Approach:
1. Reconstructing Numbers with Backward Powers of 10: 
   Used `range(len(digits) - 1, -1, -1)` combined with a multiplier (`10 ** i`) to traverse 
   from right to left and map array digits back into a full integer.
2. Understanding `range(start, stop, step)` with `(-1, -1, -1)`:
   - `start` (`len(digits) - 1`): Sets the index at the very last element of the list.
   - `stop` (`-1`): The exclusive boundary where the loop stops counting down, ensuring index `0` is included.
   - `step` (`-1`): Tells the loop to count backward by 1 at each iteration.
3. List Comprehension with `[int(char) for char in str(bgn)]`:
   A compact, elegant Pythonic tool to convert an integer to a string, iterate through every 
   individual character, cast it back to an integer, and wrap the results in a brand-new list 
   all in a single line of code.
Trade-offs: 
While slightly heavier on string conversion overhead than pure in-house arithmetic, Python handles large integer arithmetic seamlessly, making this a robust and readable alternative for managing numeric sequences.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        bgn = 0
        index = 0
        
        # Reconstruct the integer from the array digits
        for i in range(len(digits) - 1, -1, -1):
            bgn += digits[index] * (10 ** i)
            index += 1
        # Increment by one
        bgn = bgn + 1
        # Convert back into a list of integer digits using list comprehension
        return [int(char) for char in str(bgn)]
