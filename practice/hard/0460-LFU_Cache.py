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


# Solved again on 9/18
from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        """
        Option 0.
        Use a sorted dictionary 
        
        Option 1.
        1. Map key -> frequency
        2. Map frequency -> ordered dict of key-value pairs
        3. Maintain min freq 
        """
        self.min_freq = 0
        self.capacity = capacity
        self.keys = {}
        self.frequencies = {}
        
        
    def addKey(self, key, value):
        # Frequency will always start at 1
        self.keys[key] = 1
        
        # If we're adding a key, it's always the least used key
        self.min_freq = 1
        
        # Add key-value to end of ordered dict
        if 1 not in self.frequencies:
            self.frequencies[1] = OrderedDict()
        self.frequencies[1][key] = value
        
        
    def updateFrequency(self, key):
        freq = self.keys[key]
        
        value = self.frequencies[freq][key]
        
        self.frequencies[freq].move_to_end(key)
        
        self.frequencies[freq].popitem()
        
        # If this was the last key at the min frequency, update min frequency
        if len(self.frequencies[freq]) == 0 and self.min_freq == freq:
            self.min_freq += 1
            
        self.keys[key] += 1
        
        freq += 1
        
        if freq not in self.frequencies:
            self.frequencies[freq] = OrderedDict()
            
        self.frequencies[freq][key] = value

        
    def updateKey(self, key, value):
        # Update the frequency of the key to be 1 higher
        self.updateFrequency(key)
        
        # Update the key with the new value
        freq = self.keys[key]
        self.frequencies[freq][key] = value
        
        
    def evict(self):
        # Pop the least recently used key of the minimum frequency
        key, value = self.frequencies[self.min_freq].popitem(last=False)
        self.keys.pop(key)
        
        
    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        freq = self.keys[key]
        value = self.frequencies[freq][key]
        self.updateFrequency(key)
        
        return value
        
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.updateKey(key, value)
        else:
            if len(self.keys) == self.capacity and self.capacity > 0:
                self.evict()
            if self.capacity > 0:
                self.addKey(key, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
