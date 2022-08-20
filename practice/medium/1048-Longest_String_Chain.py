class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        1. put together map of len -> words
        2. keep a cache of word -> len of longest chain starting at this word
        3. for each word in words, try out all options len + 1
        4. if the option exists in the cache, return the cached value
        """
        
        from collections import defaultdict
        
        # Create map of word length -> words
        options = defaultdict(list)
        [options[len(word)].append(word) for word in words]
        
        # Create cache to save word -> longest chain
        cache = {}
        
        
        # Determine if 'a' is a predecessor of 'b'
        def predecessor(a, b):
            for i in range(len(b)):
                if b[:i] + b[i+1:] == a:
                    return True
            return False
        
        
        # Recursive function to find the longest chain of a given word
        def longest_chain(word):
            if len(word) + 1 not in options:
                return 1
            
            if word in cache:
                return cache[word]
            
            result = 1
            for option in options[len(word) + 1]:
                if predecessor(word, option):
                    result = max(result, 1 + longest_chain(option))
                
            cache[word] = result
                
            return result
        
        
        # Find the longest chain trying out each word as a potential starting word
        result = 1
        for word in words:
            result = max(result, longest_chain(word))
        
        return result
