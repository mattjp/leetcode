class Solution:
  def countElements(self, arr: List[int]) -> int:
    keys: Set[int] = set(arr)
    res: int = 0
    for a in arr:
      if a+1 in keys:
        res += 1
    return res
