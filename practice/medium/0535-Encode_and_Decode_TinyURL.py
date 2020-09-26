class Codec:
  from random import choices
  
  def __init__(self):
    self.encoding = {'': ''}
  
  def encode(self, longUrl: str) -> str:
    alphabet = 'qwertyuiopasdfghjklzxcvbnm' # Base26, add more chars to decrease collision likelihood
    key = ''
    while key in self.encoding:
      key = ''.join(choices(alphabet, k=8))
    self.encoding[key] = longUrl
    return key
        
        
  def decode(self, shortUrl: str) -> str:
    return self.encoding[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
