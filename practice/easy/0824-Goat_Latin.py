class Solution:
  def toGoatLatin(self, S: str) -> str:
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    output = []
    words = S.split(' ')
    for i,word in enumerate(words):
      a = 'a'*(i+1)
      if word[0] in vowels:
        output.append(word + 'ma' + a)
      else:
        output.append(word[1:] + word[0] + 'ma' + a)

    return ' '.join(output)
