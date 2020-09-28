class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    
    def interleave(A: str, a: int, B: str, b: int, target: str):
      for i,ch in enumerate(target):
        # if we've already tried this set of indicies, give up
        if (a,b,i) in self.seen:
          return False
        else:
          self.seen.add((a,b,i))
          
        # no chars left in A, B must match
        if a == len(A):
          return B[b:] == target[i:]
        
        # no chars left in B, A must match
        elif b == len(B):
          return A[a:] == target[i:]
        
        # recurse, because now we have 2 options (could pick from A or B)
        elif ch == A[a] == B[b]:
          return interleave(A, a+1, B, b, target[i+1:]) or interleave(A, a, B, b+1, target[i+1:])
        
        # A is the only match
        elif ch == A[a]:
          a += 1
          
        # B is the only match
        elif ch == B[b]:
          b += 1
          
        # nothing matches, give up
        else:
          return False
        
      return A == B == target
    
    # maintain set of 3 indicies, representing the space we've searched thus far
    # if we encounter a duplicate set of indicies, we can return early
    self.seen = set() 
    return interleave(s1, 0, s2, 0, s3)
