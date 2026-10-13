"""
Problem Name: Palindrome Number
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Math / Arithmetic Manipulation
- Intuition: Interviewers typically expect a solution without converting the integer 
  to a string, avoiding extra memory overhead. This is done by reversing half of 
  the integer numerically using modulo (%) and division (//) operators.
- Complexity: Time O(log10(n)) [proportional to digits], Space O(1).

Learning: 
- Intuition: Converted the integer to a string, built a character list via iteration, 
  and checked equality using Python's reverse slice `[::-1]`.
- Trade-offs: 
  - Time Complexity: O(N) where N is the number of digits.
  - Space Complexity: O(N) due to storing the string and character list (compared to O(1) math approach).
"""

class Solution(object):
    def isPalindrome(self, x):
        """:type x: int
        :rtype: bool
        """
        fnt = str(x)
        fwd = list()
        for i in fnt:
            fwd.append(i)
        if fwd == fwd[::-1]:
            return True
        else:
            return False
