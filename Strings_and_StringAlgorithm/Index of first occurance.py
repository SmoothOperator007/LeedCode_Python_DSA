"""
Problem Name: Find the Index of the First Occurrence in a String
Difficulty: Easy

--- EXPECTED / OPTIMAL APPROACH ---
Pattern: String Substring Matching / KMP Algorithm
- Intuition: The classical interview expectation is to avoid high-level built-ins and instead implement substring searching efficiently. Using the Knuth-Morris-Pratt (KMP) algorithm, we preprocess the pattern (needle) to build a Longest Prefix Suffix (LPS) table. This allows the pointer in the text (haystack) to never backtrack.
- Time Complexity: O(N + M), where N is the length of haystack and M is the length of needle.
- Space Complexity: O(M) to store the LPS array.

--- LEARNING ---
Custom Approach & Trade-offs:
- Intuition: Python's built-in substring check (`needle in haystack`) and `.index()` method delegate down to highly-optimized C implementations (often utilizing fast string searching algorithms like Boyer-Moore-Horspool under the hood). 
- Logic: The code first checks existence via `if needle in haystack:` to prevent any potential `ValueError` that `.index()` would throw if the substring is missing, then retrieves and returns the exact starting index cleanly.
- Complexity Comparison: While the theoretical worst-case time complexity of simple substring scanning/built-in search can degrade to O(N * M), in practice, Python's internal search is heavily optimized, resulting in instantaneous execution (0 ms runtime) on standard test suites while keeping code readability at a maximum.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """:type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
