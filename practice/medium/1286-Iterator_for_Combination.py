class CombinationIterator:

  def __init__(self, characters: str, combinationLength: int):
    self.combinations = list(itertools.combinations(characters, combinationLength))
    self.c = 0


  def next(self) -> str:
    output = self.combinations[self.c] if self.hasNext() else None
    self.c += 1
    return ''.join(output)


  def hasNext(self) -> bool:
    return self.c < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
