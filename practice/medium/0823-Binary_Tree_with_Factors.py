class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Sort the array
        For each element, find all of its factors that exist in the array
        If the other factor also exists in the array, add its answer to the total answer
        for this element
        Save each elements answer in a map
        """
        
        def getFactors(arr, x):
            res = []
            sqrt = int(x ** 0.5)
            for a in arr:
                if a > sqrt:
                    break
                if x % a == 0:
                    res.append(a)
            return res
            
        
        # We need to evaluate in sorted order so we solve sub-problems first
        arr.sort()
        
        # We will store the answers to sub-problems here
        ans = {}
        
        # Initially, the answer for each element is 1
        for x in arr:
            ans[x] = 1
        
        for x in arr:
            # These are all factors of x that exist in arr
            factors = getFactors(arr, x)
            
            # Given all of the factors, see if the other term exists
            for f in factors:
                t = x / f
                if t in ans:
                    m = ans[f] * ans[t]
                    if f != t:
                        m *= 2
                    ans[x] += m

        return sum(ans.values()) % 1_000_000_007
