class Solution:
  class Trie:
    def __init__(self):
      self.end = False
      self.letters = {}
      
      
    # classic trie insert
    def insert(self, word) -> None:
      def helper(trie, word) -> None:
        if len(word) == 0:
          trie.end = True
          return
        h,t = word[0], word[1:]
        if h not in trie.letters:
          trie.letters[h] = Solution.Trie()
        helper(trie.letters[h], t)
        
      helper(self, word)
      

  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    """
    - make a Trie of all words
    - read target word until invalid
    - if invalid return
    - if valid word is reached then recurse on tail of word
    - append; repeat
    """
    from collections import Counter
    
    # this is just to catch 1 stupid test case
    letters = ''.join(wordDict)
    counter = Counter(letters)
    for ch in s:
      if ch not in counter:
        return []
    
    # build our trie
    self.trie = self.Trie()
    for word in wordDict:
      self.trie.insert(word)
      
    self.output = []
    
    def dfs(ptr, s: str, cur: List[str]):
      if len(s) == 0:
        self.output.append(' '.join(cur))
        return

      for i,ch in enumerate(s):
        if ch not in ptr.letters:
          return # first characters are no longer a valid prefix, safe to exit here

        ptr = ptr.letters[ch]
        if ptr.end:
          cur.append(s[:i+1])
          dfs(self.trie, s[i+1:], cur) # always start from the root of the trie
          cur.pop()

    dfs(self.trie, s, [])
    return self.output
