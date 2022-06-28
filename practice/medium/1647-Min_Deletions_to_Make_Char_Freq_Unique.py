class Solution:
    def minDeletions(self, s: str) -> int:
        """
        If there exists a dupe freq, 
        check to see if a lower freq exists in the map
        """
        
        from collections import Counter
        
        m = {}
        d = 0
        counter = Counter(s)
        
        for ch,count in counter.items():
            while count in m:
                d += 1  # We need to delete one of these characters
                count -= 1

            # We did not need to delete all of the characters
            if count > 0:
                m[count] = ch
                
        return d
