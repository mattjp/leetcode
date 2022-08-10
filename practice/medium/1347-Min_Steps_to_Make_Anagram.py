class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        for ch,count in s_counter.items():
            if ch in t_counter:
                s_counter[ch] = max(count - t_counter[ch], 0)
                
        return sum(s_counter.values())
