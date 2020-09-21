class Solution:
  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    """
    put all trips into PQ sorted by start
    pop from PQ
    add to current cap
    add top to 2nd PQ sorted by end
    if next trip starts after top of 2PQ ends, pop from 2PQ
    else add trip to 2PQ and update cap
    return if cap > capacity
    """
    
    incomplete = [] # start, end, passengers
    inprogress = [] # end, start, passengers
    
    # build heap of incomplete trips (ordered by start)
    for p,s,e in trips:
      heapq.heappush(incomplete, (s,e,p))
    
    cur_passengers = 0
    while incomplete:
      start, end, passengers = heapq.heappop(incomplete) # next available trip
      
      # this trip starts after trip that ends earliest
      # therefore, we will have some seats free up
      while inprogress and start >= inprogress[0][0]: 
        _,_,p = heapq.heappop(inprogress)
        cur_passengers -= p
      
      cur_passengers += passengers # add new passengers to the vehicle and check constraints
      if cur_passengers > capacity:
        return False

      heapq.heappush(inprogress, (end, start, passengers)) # this trip is now in progress
      
    return True
