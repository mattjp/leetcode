class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    # all lower case
    if word.lower() == word:
      return True
    # all capital
    elif word.upper() == word:
      return True
    # first capital
    elif word[0].upper() == word[0] and word[1:].lower() == word[1:]:
      return True
    # false
    else:
      return False
