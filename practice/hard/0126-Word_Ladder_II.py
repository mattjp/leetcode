class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    """
    BFS, going layer by layer
    after each set of words of length n are processed, remove all searched words from the search space
    repeat until the end word is found, then break as this will be the shortest path
    
    this is definitely sub-optimal
    """
    
    from collections import deque
        
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    word_list = set(wordList) # will act as current search-space
    queue = deque([[beginWord]]) # ([words])
    # seen = set([beginWord])
    output = []
    min_len = len(word_list)+1
    level = 1
    visited = set()
    
    if endWord not in word_list:
      return []
    
    while queue:
      words = queue.popleft()
      
      # remove all seen words from the search space if we have reached a new level
      # terminate if we have seen a solution
      if len(words) > level:
        for v in visited:
          if v in word_list:
            word_list.remove(v)
        visited = set()
        if len(words) >= min_len:
          break
        else:
          level += 1
          
      # add all new word combos
      word = words[-1]
      for i in range(len(word)):
        for ch in alphabet:
          new_word = word[:i] + ch + word[i+1:]
          if new_word in word_list:
            visited.add(new_word)
            new_words = words + [new_word]
            queue.append(new_words)
            if new_word == endWord:
              min_len = len(new_words)
              output.append(new_words)

    return output
