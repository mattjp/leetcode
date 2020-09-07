class Solution:
  def wordPattern(self, pattern: str, str: str) -> bool:
    word_map = {}
    pattern_map = {}
    words = str.split(' ')

    if len(words) != len(pattern):
      return False
    
    for i,word in enumerate(words):
      p = pattern[i % len(pattern)]
      if p not in pattern_map:
        pattern_map[p] = word
      if word not in word_map:
        word_map[word] = p
        
      if word != pattern_map[p] or p != word_map[word]:
        return False
      
    return True
