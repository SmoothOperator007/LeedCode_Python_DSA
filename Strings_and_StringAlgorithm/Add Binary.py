"""
Problem: [67. Add Binary]
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: Two-Pointer Bitwise Simulation / Right-to-Left Carry Addition
Intuition: 
Initialize two pointers at the last characters of strings `a` and `b` and a carry variable set to 0. 
Iterate backward until both strings and any remaining carry are exhausted. At each step, extract 
the current digits, sum them up along with the carry, compute the new bit using modulo 2 (`% 2`), 
and update the carry using integer division (`// 2`).

Time Complexity: O(max(N, M)) where N and M are the lengths of strings a and b.
Space Complexity: O(max(N, M)) to store the resulting binary string output.

--- LEARNING ---
My Custom Approach & Implementation:
1. Base-2 Parsing (`int(a, 2)`): 
   Quickly converts a binary string into a base-10 integer by specifying the base parameter.
2. Direct Addition: 
   Leverages Python's native capability to handle arbitrarily large integers automatically without overflow.
3. Binary Formatting (`bin(...)`): 
   Instantly transforms the computed sum back into Python's standard binary representation string (which always begins with the prefix `"0b"`).
4. String Slicing (`[2:]`): 
   A concise Pythonic trick to strip away the leading `"0b"` prefix, leaving only the raw binary characters required for the solution output.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers, add them, convert back to binary, and drop '0b'
        c = bin(int(a, 2) + int(b, 2)) #we can put [2:] directly here without introducing c
        return c[2:]
