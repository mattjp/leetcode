class WordDictionary:
  class Trie:
    def __init__(self):
      self.letters = {}
      self.end = False
      
      
    def insert(self, word: str) -> None:
      """
      normal trie insertion
      """
      def helper(trie: 'Trie', word: str) -> None:
        if len(word) == 0:
          trie.end = True
          return
        
        h,t = word[0], word[1:]
        if h not in trie.letters:
          trie.letters[h] = WordDictionary.Trie()
        helper(trie.letters[h], t)
      
      # run the helper
      helper(self, word)
        

    def search(self, string) -> bool:
      """
      if string is empty, return true
      if h not in trie.letters, return false
      if h in trie, recurse string=t
      if h==. then for letter in letters recurse, if any return True, return
      """

      def helper(trie: 'Trie', string: str) -> bool:
        if len(string) == 0:
          return trie.end
        
        h,t = string[0], string[1:]
        if h == '.':
          return any([helper(trie.letters[letter], t) for letter in trie.letters])  
        elif h not in trie.letters:
          return False
        else:
          return helper(trie.letters[h], t)
        
      # run the helper
      return helper(self, string)


  def __init__(self):
      """
      Initialize your data structure here.
      """
      self.trie = WordDictionary.Trie()


  def addWord(self, word: str) -> None:
      """
      Adds a word into the data structure.
      """
      self.trie.insert(word)


  def search(self, word: str) -> bool:
      """
      Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
      """
      return self.trie.search(word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
