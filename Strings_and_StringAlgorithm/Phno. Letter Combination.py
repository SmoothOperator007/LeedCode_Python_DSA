"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH (Backtracking / DFS) ---
Pattern: Decision Tree & Backtracking
Intuition: 
  Each number on the phone gives us a few letters to choose from.
  Instead of getting tangled in nested loops, we use a recursive function to build a combination letter-by-letter.
  As soon as our built string matches the total number of input digits, we save it to our results and step backward to try the next available letter combination.

Time Complexity: O(4^N * N), where N is the length of digits. In the worst case (e.g., all '7's or '9's), 
                 each digit has 4 choices, and building each string takes O(N) time. Given N <= 4, 
                 this is bounded and extremely fast.
Space Complexity: O(N) for the recursive call stack depth and storing the active combination path.

--- LEARNING ---
Custom Iterative Approach (BFS Layer Expansion):
  - We Used Loop method of strings. Firstly we define dictionary which holds letters for each number.
    Then we make 1st loop to iterate through the numbers, then 2nd loop (IMP LOOP) which looks backward at what you already built in the previous step, so as to 
    add the new letters combination and finally the 3rd loop looks at the current digit's letters (e.g., 'd', 'e', 'f') and glues every single one of them onto the
    base combination pulled from Tier 2.
  - Trade-offs: This avoids any risk of stack overflow and matches a clean queue expansion model. 
    Because LeetCode constraints limit `digits.length <= 4`, both iterative and recursive approaches 
    perform nearly identically in practice (0 ms runtime).
"""


class Solution(object):

  def letterCombinations(self, digits):
    """:type digits: str

    :rtype: List[str]
    """
    if not digits:
      return []

    nums = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    current_combinations = [""]

    for d in digits:
      next_combinations = []
      for combo in current_combinations:
        for letter in nums[d]:
          next_combinations.append(combo + letter)
      current_combinations = next_combinations

    return current_combinations

    # --- ALTERNATIVE RECURSIVE BACKTRACKING APPROACH ---
    # result = []
    #
    # def backtrack(index, path):
    #     # Base case: if path length matches digits length, we found a combination
    #     if index == len(digits):
    #         result.append(path)
    #         return
    #
    #     # Explore all letter choices for the current digit
    #     for letter in nums[digits[index]]:
    #         backtrack(index + 1, path + letter)
    #
    # backtrack(0, "")
    # return result
