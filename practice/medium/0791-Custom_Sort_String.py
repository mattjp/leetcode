class Solution:
    def customSortString(self, order: str, s: str) -> str:        
        from collections import Counter
        
        order_set = set(order)
        s_dict = Counter(s)
        
        ans = ""
        
        for ch in order:
            if ch in s_dict:
                # we may need to add more than 1 letter in sorted order
                ans += ch * s_dict[ch]
                
        for ch in s:
            if ch not in order_set:
                ans += ch
                
        return ans
        
