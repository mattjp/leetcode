class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        You can combine all the words from `words2`, using the maximum count of each character.
        If that invariant holds, then you know the word is a subset of all the words in `words2`
        """
        from collections import Counter
        
        def is_subset(a, b):
            for ch,count in b.items():
                if ch not in a:
                    return False
                if a[ch] < count:
                    return False
                
            return True
        
        output = []
        superset = Counter(words2[0])
        for w in words2[1:]:
            wc = Counter(w)
            for ch,count in wc.items():
                if ch not in superset:
                    superset[ch] = count
                else:
                    superset[ch] = max(superset[ch], count)
        
        for w in words1:
            if is_subset(Counter(w), superset):
                output.append(w)
                
        return output
