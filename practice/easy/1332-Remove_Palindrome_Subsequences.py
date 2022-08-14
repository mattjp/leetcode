class Solution:
    """
    This problem is dumb. Substrings can be created by deleting any number of 
    characters. Since there are only 2 possible characters, the max number of
    steps is 2.
    """
  
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2
