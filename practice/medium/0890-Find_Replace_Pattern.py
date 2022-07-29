class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        def translate(s):
            l = 0
            m = {}
            o = ''
            for ch in s:
                if ch not in m:
                    m[ch] = letters[l]
                    l += 1
                o += m[ch]
            return o
                    
            
        output = []
        tp = translate(pattern)
        for word in words:
            tw = translate(word)
            if tp == tw:
                output.append(word)
                
        return output
