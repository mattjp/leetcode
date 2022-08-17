class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        m = {}
        i = 1
        
        for n in s:
            if n not in m:
                m[n] = i
                i += 1
            
        return list(map(lambda a: m[a], arr))
