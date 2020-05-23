class Solution:
  def longestPalindrome(self, s: str) -> str:

    def palindromeFromIndex(s: str, l: int, r: int) -> str:
      while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
      return s[l+1:r] # negate the last `l -= 1, r += 1` since while loop fails after l,r are set

    output = ''
    for i in range(len(s)):
      x = palindromeFromIndex(s, i, i) # check same starting index
      y = palindromeFromIndex(s, i, i+1) # check side-by-side
      cur = x if len(x) >= len(y) else y
      output = cur if len(cur) > len(output) else output
    return output
