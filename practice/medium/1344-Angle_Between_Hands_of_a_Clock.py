class Solution:
  def angleClock(self, hour: int, minutes: int) -> float:
    mdeg = minutes * 6.0
    hdeg = (minutes * 0.5) + ((hour % 12) * 30.0) # mod 12 so 12 -> 0
    angle = abs(hdeg - mdeg)
    return (360.0 - angle) if angle > 180.0 else angle  # always take acute angle
