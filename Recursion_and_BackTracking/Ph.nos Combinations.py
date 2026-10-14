"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium

--- RECURSIVE / BACKTRACKING APPROACH ---
Pattern: Decision Tree & Backtracking

Time Complexity: O(4^N * N), where N is the length of digits. In the worst case (e.g., digits like '7' or '9'), 
                 each number has 4 choices, and building each final string takes O(N) time. Since N <= 4, 
                 this runs instantly.
Space Complexity: O(N) for the recursive call stack depth and storing the active path string.

STEP BY STEP BREAKDOWN OF CODE:- thinking of example - digits: "23"
It starts by defining a backtracting function with index and current_string as arguments, then a condition comes where if the index has reached the end then it
appends to another empty list outside the function. Then comes the main Logic where a variable letter contains the letters of the first digit defined, 
then we initiate a loop which iterates through the letters of the first digit, which then recalls the backtrace function but with arguments index+1 and 
current_string+letter i.e "" + "a". Notice that we first called the backtrace function with arguments index = 0  and an empty string "". So now we the new arguements, 
the indexis 1 which is not len(digits), so now the letters function will have letters of 2nd digit, then again we initiate the loop on the letters of the 2nd digit,
which then again recalls backtrace 2nd time but this time index is 2 is equal to len(digits) so appends the result of the current_string+letter i.e "a" + "d" = "ad"
to empty list result which is outside the functions so it cannot be changed. Now it hits return AND RETURN DOSENT STOP THE FUNCTION, IT GOES BACK THE THE PREVIOUS 
LOOP WHICH WAS UNFINISHED I.E THE 2ND LOOP. This time the current_string still has "a" but letter is "e" now so it again recalls just to put "ae" to result list, 
then again GOES BACK to the 2nd loop untill it is over and result has ["ad", "ae", "af"] now when considering it retraces back to 2nd loop after return, and since
the 2ND LOOP IS OVER IT GOES BACK TO 1ST LOOP WHICH IS UNFINISHED AND CHOOSES "b" and then again continues this process of recursion untill, result has all the 
possible outcomes.
THIS IS RECURSION.
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

    result = []

    # Helper function for recursive backtracking
    def backtrack(index, current_string):
      # Base Case: When our built string has the same length as digits,
      # we've reached the end of a valid path. Save it and return!
      if index == len(digits):
        result.append(current_string)
        return

      # Get the letters mapped to the current digit index
      letters = nums[digits[index]]

      # Try every letter choice for this digit one by one
      for letter in letters:
        # Move forward to the next digit (index + 1) and add the letter to our path
        backtrack(index + 1, current_string + letter)

    # Start recursion at index 0 with an empty string
    backtrack(0, "")
    return result
