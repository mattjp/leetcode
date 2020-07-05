class Solution:
  def nthUglyNumber(self, n: int) -> int:
    """
    Maintain a list (uglies) of all ugly numbers thus far.
    Keep track of 3 pointers in uglies - one for 2, 3, and 5.
    We know the next smallest ugly number will be a previous ugly number
    multiplied by 2, 3, or 5.
    Add the smallest number of p2 * 2, p3 * 3, and p5 * 5 to uglies.
    """
    
    p2 = p3 = p5 = 0
    uglies = [1]

    # iterate until we have `n` ugly numbers
    while len(uglies) < n:
    
      # if p2 * 2 is the smallest ugly number, append and increment
      if uglies[p2]*2 <= min(uglies[p3]*3, uglies[p5]*5):
        if uglies[-1] != uglies[p2]*2: 
          uglies.append(uglies[p2]*2)
        p2 += 1
      
      # if p3 * 3 is the smallest ugly number, append and increment
      elif uglies[p3]*3 <= min(uglies[p2]*2, uglies[p5]*5):
        if uglies[-1] != uglies[p3]*3: 
          uglies.append(uglies[p3]*3)
        p3 += 1
        
      # if p5 * 5 is the smallest ugly number, append and increment
      else:
        if uglies[-1] != uglies[p5]*5: 
          uglies.append(uglies[p5]*5)
        p5 += 1

    # return n-th ugly number
    return uglies[-1]
