class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
    class Trie:
      """
      use a Trie to efficiently store letter combinations
      """
      def __init__(self):
        self.letters = {}
        self.end = False
        
      def insert(self, word):
        def helper(trie, word):
          if len(word) == 0:
            trie.end = True
            return
          h,t = word[0], word[1:]
          if h not in trie.letters:
            trie.letters[h] = Trie()
          helper(trie.letters[h], t)
        helper(self, word)
     
    
    def dfs(i: int, j: int, ptr: Trie, cur: str, visited: set):
      """
      DFS through the board, stopping when:
        - out-of-bounds
        - letter sequence does not exist in the Trie
        - letter was already used in the current sequence
      add all valid words found during the DFS
      """
      if (
        i < 0 or
        j < 0 or
        i > len(board)-1 or
        j > len(board[0])-1 or
        (i, j) in visited or 
        board[i][j] not in ptr.letters
      ):
        return
      
      letter = board[i][j]
      cur += letter
      next_ptr = ptr.letters[letter]
      visited.add((i, j))
      
      if next_ptr.end and cur not in self.found:
        self.output.append(cur)
        self.found.add(cur)
      
      dfs(i-1, j, next_ptr, cur, visited)
      dfs(i, j+1, next_ptr, cur, visited)
      dfs(i+1, j, next_ptr, cur, visited)
      dfs(i, j-1, next_ptr, cur, visited)
      
      visited.remove((i, j))

    # build the Trie  
    self.trie = Trie()  
    for word in words:
      self.trie.insert(word)

    # try to find words starting at every board index
    self.output = []
    self.found = set()
    for i in range(len(board)):
      for j in range(len(board[0])):
        dfs(i, j, self.trie, '', set())
        
    return self.output
