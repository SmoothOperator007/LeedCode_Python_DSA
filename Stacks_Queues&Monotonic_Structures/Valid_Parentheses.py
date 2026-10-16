"""
Problem: Valid Parentheses (LeetCode 20)
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Stack (LIFO)
Intuition: 
Parentheses matching inherently requires a Last-In, First-Out structure because the most recently opened bracket must be the first one closed. 
As we scan the string from left to right:
1. When an opening bracket is encountered, we store it in a stack.
2. When a closing bracket is encountered, we inspect the top of the stack. If the stack is empty or the top element does not match the expected corresponding opening bracket, the sequence is invalid.
3. At the end of the loop, the stack must be completely empty; otherwise, unclosed opening brackets remain.

Complexities:
- Time Complexity: O(N) because we iterate through the string of length N once, performing O(1) append/pop operations on the stack.
- Space Complexity: O(N) in the worst-case scenario where the string consists entirely of opening brackets.

--- LEARNING ---
My Custom Intuition & Troubleshooting Journey:
- Initially attempted validating strings via fixed-step index increments (adjacent pairs), which failed because nested structures (e.g., "([{}])") don't place matching partners adjacently.
- Recognized the need for a dynamic tracking structure (a stack list) rather than fixed comparisons.
- Learned the importance of guarding against `IndexError` by checking `if not estack` *before* attempting to peek at `estack[-1]` when a stray closing bracket appears at the start or during the sequence.
- Used 'return not estack' instead of just 'True' as if estack is empty return false.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sdict = {'(': ')', '{': '}', '[': ']'}
        estack = []
        
        for i in s:
            if i in sdict:
                estack.append(i)
            else:
                if not estack or sdict[estack[-1]] != i:
                    return False
                estack.pop()
                
        return not estack
