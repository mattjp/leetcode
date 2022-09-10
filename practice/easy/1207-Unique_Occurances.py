class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        keys = set(c.keys())
        vals = set(c.values())
        return len(keys) == len(vals)
        
