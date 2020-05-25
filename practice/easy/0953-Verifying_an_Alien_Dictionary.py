class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:

    for i in range(1, len(words)):
      word0 = words[i-1]
      word1 = words[i]

      j = 0
      stop = min(len(word0), len(word1))
      while j < stop and word0[j] == word1[j]:
        j += 1

      # found a difference before the end of the word
      if j < stop:
        i1 = order.index(word0[j])
        i2 = order.index(word1[j])
        if i1 > i2:
          return False
      # no differences were found before one word ran out of characters
      else:
        # if the first word was longer, it is always not true
        if len(word0) > len(word1):
          return False
        # otherwise, make sure the last characters are equal
        else:
          return word0[j-1] == word1[j-1]

    return True
