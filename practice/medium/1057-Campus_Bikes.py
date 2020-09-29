class Solution:
  def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    """
    PQ of (dist, worker, bike)
    pop top - if bike is taken or worker is done, continue
    since N<=M, there is guaranteed to be enough bikes 
    """
    heap = []
    
    for w,worker in enumerate(workers):
      for b,bike in enumerate(bikes):
        d = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
        heap.append((d,w,b))

    heap.sort()
    output = {}
    available = set(range(len(bikes)))
    
    # for some reason, using a queue here was too slow?
    for d,w,b in heap:
      if w not in output and b in available:
        output[w] = b
        available.remove(b)

    return [output[i] for i in range(len(workers))]
