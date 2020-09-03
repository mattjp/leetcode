class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    define mapping of wildcard -> words
    starting at beginWord, iterate through all possible wildcards
    enqueue all possible words, along with their depth
    """
    from collections import defaultdict, deque
    
    if endWord not in wordList:
      return 0
    
    L = len(beginWord) # all words are same length
    
    wildcards = defaultdict(list) # map wildcard -> list of words that can be made from wildcard
    for word in wordList:
      for i in range(L):
        wildcard = word[:i]+'*'+word[i+1:]
        wildcards[wildcard].append(word)
        
    
    queue = deque([(beginWord, 1)]) # maintain depth along with current word for BFS
    
    while queue:
      top_word, depth = queue.popleft()
      
      for i in range(L): # search all wildcards of the current word, add them to the queue
        wildcard = top_word[:i]+'*'+top_word[i+1:]
        next_words = wildcards[wildcard]
        wildcards[wildcard] = [] # do not search for this wildcard again
        
        for next_word in next_words: # check if we have found the target word
          if next_word == endWord:
            return depth+1
          queue.append((next_word, depth+1))
          
    return 0
