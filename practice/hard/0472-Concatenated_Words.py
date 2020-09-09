# note: this was only faster than 5% of solutions, so it's probabaly
# a little incorrect/inefficent somewhere.
# i'm guessing it's due to not storing a pointer in the trie while
# calculating prefixes.

class Solution:
  
  # create a Trie so we can check if words are words quickly
  # this is just the basic Trie from the Trie question, except
  # the prefix function returns the Trie object so we can check
  # if it's the end of the word quickly.
  class Trie:
    def __init__(self):
      self.end = False
      self.letters = {}
      
    def insert(self, word: str) -> None:
      def go(cur, word):
        if len(word) == 0:
          cur.end = True
          return
        h,t = word[0], word[1:]
        if h not in cur.letters:
          cur.letters[h] = Solution.Trie()
        go(cur.letters[h], t)
      go(self, word)
      
    # return Trie at end-of-word if it exists. otherwise return None.
    def prefix(self, word: str) -> 'Trie':
      def go(cur, word):
        if len(word) == 0:
          return cur
        h,t = word[0], word[1:]
        if h not in cur.letters:
          return None
        return go(cur.letters[h], t)
      return go(self, word)
      
  
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

    # DFS to see if a word is concatenated from other words in the Trie.
    # algo:
    #   - while the prefix of the current word exists in the Trie, continue
    #   - if the prefix is a full word in the Trie, recurse
    #   - if the recursive call returns True, we know the remainder of the word
    #     represents a concatenation, so we can exit the loop early
    #   - if the recursive call returns False, we continue iterating, to check 
    #     other, longer words
    def concatenated(word, count=0) -> bool:
      if len(word) == 0:
        return True if count > 1 else False
      i = 1
      while i <= len(word):
        prefix = trie.prefix(word[:i])
        if not prefix:
          return False
        if prefix.end:
          if concatenated(word[i:], count+1): 
            return True
        i += 1
      return False
      
    # instantiate the Trie and insert all given words
    trie = self.Trie()
    for word in words:
      trie.insert(word)
    
    # for each word, see if it is the concatenation of other words
    output = []
    for word in words:
      if concatenated(word):
        output.append(word)

    return output
