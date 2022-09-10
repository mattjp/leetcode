class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        It would be smarted to use a queue, push/pop is O(1)
        Every kth pop, just don't push
        """
        
        from sortedcontainers import SortedSet
        
        s = SortedSet(range(n))
        i = 0
        
        
        while len(s) > 1:
            i = (i + k - 1) % len(s)
            s.pop(i)
            
        return s[0]+1
