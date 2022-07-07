class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        set i=0, iterating through s3
        assume we're starting with s1
        while s1[0:i] == s3[0:i]
            if s2[0] == s3[i+1]
            
            
        take the longest common substring you can from s1 and s3
        if the next character isn't the first character in s2 -- go backward one character until true
        
        i=j=0, while s1[i] == s3[i] then if s3[i+1] == s2[j] add to search set, i++
        
        we want the search set to try the longest possible interleavings first
        """
        
        def go(a, b, result, r):
            """
            @param a - the string we are currently adding to the result string
            @param b - the other string we'll look at the first character of to determine if the interleaving
                       is invalid
            @param result - the result string we're trying to create
            @param r - the index of the result string we're currently investigating
            """
            
            
            # base case: if the remaining result is equal to what we need to add
            if len(a) < 1:
                return b == result[r:]
            if len(b) < 1:
                return a == result[r:]
            
            for i in range(len(a)):
                # longest matching substring or we've seen this combo before
                if a[i] != result[r+i] or (a[i+1:], b) in seen:
                    return False

                # interleaving is valid
                if result[r+i+1] == b[0]:
                    seen.add((a[i+1:], b))  # save the remaining substring of a and all of b
                    if go(b, a[i+1:], result, r+i+1):  # break as soon as we find True
                        return True
                    
        seen = set()
        if len(s3) == len(s1) + len(s2):
            return go(s1, s2, s3, 0) or go(s2, s1, s3, 0)  # 2 starting cases, either s1 or s2 is added first
        return False
