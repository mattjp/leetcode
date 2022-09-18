class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = set()
        
        for word in words:
            m = ''
            for ch in word:
                m += morse[ord(ch)-97]  # ord('a') == 97
            ans.add(m)
            
        return len(ans)
