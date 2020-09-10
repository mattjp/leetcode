class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    
    from collections import Counter
    scounter = Counter(secret)
    
    cows = 0
    bulls = 0
    for s,g in zip(secret, guess):
      if s == g:
        bulls += 1
        if scounter[g] == 0:
          cows -= 1
        else:
          scounter[g] -= 1
      elif g in scounter:
        if scounter[g] > 0:
          cows += 1
          scounter[g] -= 1
        
    return '%iA%iB' % (bulls, cows)
