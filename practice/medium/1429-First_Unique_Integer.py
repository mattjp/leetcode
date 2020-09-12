class FirstUnique:
  """
  use ordered dict to keep track of unique values in the order they were added.
  use set of ints to keep track of all duplicate values.
  """
  from collections import OrderedDict
  
  def __init__(self, nums: List[int]):
    self.unique = OrderedDict()
    self.duplicate = set()
    for num in nums:
      self.add(num)


  def showFirstUnique(self) -> int:
    return next(iter(self.unique)) if len(self.unique) > 0 else -1

    
  def add(self, value: int) -> None:
    if value in self.duplicate:
      return
    elif value in self.unique:
      self.duplicate.add(value)
      self.unique.pop(value)
    else:
      self.unique[value] = True
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
