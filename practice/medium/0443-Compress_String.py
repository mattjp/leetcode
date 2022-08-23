class Solution:
    def compress(self, chars: List[str]) -> int:
        
        cur = None
        count = 0
        s = ''
        
        for ch in chars:
            if cur == None:
                cur = ch
                count = 1
            elif cur == ch:
                count += 1
            else:
                s += cur
                if count > 1:
                    s += str(count)
                cur = ch
                count = 1
                
        s += cur
        if count > 1:
            s += str(count)
        
        for i, ch in enumerate(s):
            chars[i] = ch
            
        return len(s)
