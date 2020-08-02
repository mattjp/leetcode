class MyHashSet:

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.p = 104729 # big prime to reduce collisions
    self.hash_set = [[]] * self.p # use separate chaining collision handling


  def add(self, key: int) -> None:
    if not self.contains(key):
      self.hash_set[key % self.p].append(key)

  def remove(self, key: int) -> None:
    if self.contains(key):
      self.hash_set[key % self.p].remove(key)


  def contains(self, key: int) -> bool:
    """
    Returns true if this set contains the specified element
    """
    return True if key in self.hash_set[key % self.p] else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
