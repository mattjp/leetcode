class LFUCache:

  def __init__(self, capacity: int):
    self.freqs = {1: OrderedDict()} # map frequency to key (in the order they were added)
    self.keys = {} # map key to (freq, value)
    self.min_freq = 1
    self.cap = capacity


  def update_freq(self, key: int, value: int) -> int:
    (freq, val) = self.keys[key] # get current frequency and value of the given key
    self.keys[key] = (freq+1, value) # update frequency and value (if needed) for the key

    freq_keys = self.freqs[freq] # get all keys that have the keys previous frequency 
    freq_keys.pop(key) # remove the key from the list of frequencies

    # if this key was the last key at this frequency
    # and it is the minimum frequency, add 1 to minimum frequency
    if len(freq_keys) == 0 and self.min_freq == freq: 
      self.min_freq += 1

    # add a new key list to freqs, if there are no other keys at the new frequency
    if freq+1 not in self.freqs:
      self.freqs[freq+1] = OrderedDict()

    self.freqs[freq+1][key] = True # add the key to its new frequency list (True doesn't matter, just needs a value)
    return val


  def get(self, key: int) -> int:
    if key not in self.keys:
      return -1
    return self.update_freq(key, self.keys[key][1]) # update frequency, not value


  def put(self, key: int, value: int) -> None:
    if self.cap == 0: # this covers a stupid test
      return

    # evict, if necessary
    # eviction happens by popping the LRU item from the list of frequencies at the minimum frequency
    if len(self.keys) == self.cap and key not in self.keys:
      target,_ = self.freqs[self.min_freq].popitem(last=False)
      self.keys.pop(target)

    # if the key is not in the cache, update frequency: 1
    if key not in self.keys:
      self.keys[key] = (1, value)
      self.freqs[1][key] = True
      self.min_freq = 1
    else:
      self.update_freq(key, value) # update key with new value and update its frequency


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
