# Remove all occurances of "AA", "BB", or "CC" from a string

def solution(S):
  while "AA" in S or "BB" in S or "CC" in S:
    S = S.replace("AA", "")
    S = S.replace("BB", "")
    S = S.replace("CC", "")
  return S
