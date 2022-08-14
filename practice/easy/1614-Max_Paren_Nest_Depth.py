class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        b = 0
        for ch in s:
            if ch == '(':
                c += 1
                b = max(b, c)
            elif ch == ')':
                c -= 1
                
        return b
