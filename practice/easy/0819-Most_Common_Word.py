class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # given punctuation
    punctuation = '!?\',;.'

    # remove punctuation from paragraph
    no_punctuation = ''
    for ch in paragraph:
      no_punctuation += ch if ch not in punctuation else ' '

    # remove leading/trailing whitespace, lowercase, split into array
    words = no_punctuation.strip().lower().split(' ')

    # filter out spaces from words
    words = list(filter(lambda ch: ch != '', words))
    
    # count unique words
    counter = collections.Counter(words)

    # remove banned words from counter
    for ban in banned:
      if ban in counter:
        del counter[ban]
    
    # return most common, a list of tuples of length 1
    return counter.most_common(1)[0][0]
