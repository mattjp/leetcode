class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda w: w[::-1], s.split(" "))))
      
