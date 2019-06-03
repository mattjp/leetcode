# Given a string and a list of words, find the shortest substring such that the
# substring contains all words present in the list.

class Solution:
  # All previously checked substrings.
  seen = set()

  # Check if text still contains all words.
  def contains(self, text, words):
    all_words = text.split(" ")
    for word in words:
      if word not in all_words:
        return False
    return True

  # Return the shortest substring by removing the last and first letter.
  def helper(self, text, prev_text, words):
    if not self.contains(text, words):
      return prev_text
    del_last = text.rsplit(" ", 1)[0]
    del_first = text.split(" ", 1)[1]
    if del_last not in self.seen:
      self.seen.add(del_last)
      del_last = self.helper(del_last, text, words)
    if del_first not in self.seen:
      self.seen.add(del_first)
      del_first = self.helper(del_first, text, words)
    return min([del_last, del_first], key=len)

  # Returns the minimum substring such that all words are still present.
  def find_substring(self, text, words):
    return self.helper(text, text, words)


def main():
  s = Solution()
  t = "the rain in spain causes pain in maine"
  w = ["spain", "causes", "in"]
  result = s.find_substring(t, w)
  print(result)

if __name__ == "__main__":
  main()