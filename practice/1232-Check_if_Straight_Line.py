class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

    def getSlope(x1: int, y1: int, x2: int, y2: int) -> float:
      if x2 == x1:
        return float('inf')
      return (y2-y1) / (x2-x1)

    prev_slope = None
    for i in range(len(coordinates)-1):
      p1 = coordinates[i]
      p2 = coordinates[i+1]
      slope = getSlope(p1[0],p1[1],p2[0],p2[1])
      if slope != prev_slope and prev_slope != None:
        return False
      prev_slope = slope
    return True
