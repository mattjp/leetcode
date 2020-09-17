class FreqStack:
  from collections import defaultdict
  
  def __init__(self):
    self.keys = defaultdict(int) # map key to frequency
    self.freqs = defaultdict(list) # map frequency to list of keys at this frequency
    self.max_freq = 0


  def push(self, x: int) -> None:
    """
    add 1 to the old frequency
    update frequency of the key
    append the key to the updated frequency
    note: we don't delete the entry from the previous frequency, because if this element gets popped,
          we can rely on its previous entry at the lower frequency
    """
    new_freq = self.keys[x] + 1
    self.keys[x] = new_freq
    self.freqs[new_freq].append(x)
    self.max_freq = max(self.max_freq, new_freq)

  def pop(self) -> int:
    """
    removes and returns the most frequent element in the stack
    tie goes to most most recently added
    if the last element of a frequency is removed, we know the next maximum frequency must be one lower
    """
    x = self.freqs[self.max_freq].pop()
    new_freq = self.keys[x] - 1
    self.keys[x] = new_freq
    if len(self.freqs[self.max_freq]) == 0:
      self.max_freq -= 1
    return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
