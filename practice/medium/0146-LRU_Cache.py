# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:

  def __init__(self, capacity: int):
    self.key_values = {}
    self.most_recent = []
    self.capacity = capacity
    self.weight = 0

  def update_most_recent(self, key: int) -> None:
    self.most_recent = list(map(lambda x: (self.weight, x[1]) if x[1] == key else x, self.most_recent))
    self.most_recent.sort()
    self.weight += 1

  def get(self, key: int) -> int:
    if key in self.key_values:
      self.update_most_recent(key)
      return self.key_values[key]
    return -1

  def put(self, key: int, value: int) -> None:
    if len(self.most_recent) == self.capacity:
      if key not in self.key_values:
        (_, most_recent_key) = heapq.heappop(self.most_recent)
        del self.key_values[most_recent_key]
        self.key_values[key] = value
        heapq.heappush(self.most_recent, (self.weight, key))
        self.weight += 1
      else:
        self.update_most_recent(key)
        self.key_values[key] = value
    else:
      if key not in self.key_values:
        self.key_values[key] = value
        heapq.heappush(self.most_recent, (self.weight, key))
        self.weight += 1
      else:
        self.update_most_recent(key)
        self.key_values[key] = value
        
# solved again - correctly with external libraries
class LRUCache:
  from collections import OrderedDict

  def __init__(self, capacity: int):
    self.cache = OrderedDict() # keep cache in insertion order
    self.capacity = capacity


  def get(self, key: int) -> int:
    if key in self.cache:
      self.cache.move_to_end(key, last=False) # move cache[key] to the head of the dict
      return self.cache[key]
    else:
      return -1


  def put(self, key: int, value: int) -> None:
    self.cache[key] = value
    self.cache.move_to_end(key, last=False) # move cache[key] to the head of the dict
    if len(self.cache) > self.capacity:
      self.cache.popitem(last=True) # pop the least recently used item

# solved the hard way - building out OrderedDict
class dll_node:
  def __init__(self, key=-1, val=-1):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None


class LRUCache:
  def __init__(self, capacity: int):
    self.cache = {} # int -> DLL node
    self.capacity = capacity

    # doubly-linked list
    self.head = dll_node()
    self.tail = dll_node()
    self.head.next = self.tail
    self.tail.prev = self.head
        
  def pop_tail(self):
    p = self.tail.prev
    p.prev.next = self.tail
    self.tail.prev = p.prev
    return p
        
  def move_to_head(self, key: int) -> None:
    node = self.cache[key]

    # if the node previously existed in the DLL -- delete it
    if node.prev != None and node.next != None:
      p = node.prev
      n = node.next
      p.next = n
      n.prev = p
        
    # set the `next` pointer of the DLL head to the node
    h = self.head.next    # old head
    node.next = h         # new head next -> old head
    h.prev = node         # old head previous -> new head
    node.prev = self.head # new head prev -> DLL head
    self.head.next = node # DLL head next -> new head

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    self.move_to_head(key)
    return self.cache[key].val
        
  def put(self, key: int, value: int) -> None:
    # create a new node if one does not exist
    if key not in self.cache:
      self.cache[key] = dll_node(key,value)
    else:
      self.cache[key].val = value

    # update head of DLL
    self.move_to_head(key)

    # remove least-recently used
    if len(self.cache) > self.capacity:
      t = self.pop_tail()
      del self.cache[t.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
