class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    from collections import Counter
    
    sorted_words = sorted(words) # this step can be avoided by using a heap
    c = Counter(sorted_words)
    most_common = c.most_common(k)
    
    return list(map(lambda x: x[0], most_common))
