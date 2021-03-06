class Solution:
  def rotateString(self, A: str, B: str) -> bool:
    if A == B:
      return True
    
    for i in range(len(A)):
      rotated = A[i:] + A[:i]
      if rotated == B:
        return True
      
    return False
