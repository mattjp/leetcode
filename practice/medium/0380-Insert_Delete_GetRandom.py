class RandomizedSet:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.random_set = {}
    self.elements = []

  def insert(self, val: int) -> bool:
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    """
    if val not in self.random_set:
      self.elements.append(val)
      self.random_set[val] = len(self.elements)-1
      return True
    return False
        

  def remove(self, val: int) -> bool:
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    """
    if val in self.random_set:
      i = self.random_set[val]  # get index of element in array
      elem = self.elements[i]   # get element to delete
      tail = self.elements[-1]  # get element to swap
      self.elements[i] = tail   # swap
      self.elements.pop()       # pop tail
      self.random_set[tail] = i # update index of tail in set
      del self.random_set[val]  # remove old key from set
      return True
    return False
        

    def getRandom(self) -> int:
      """
      Get a random element from the set.
      """
      return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
