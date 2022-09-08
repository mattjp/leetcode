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
  
  
# Solved again 9-9-22
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Put all trips into a heap
        Sort the heap with smallest start on top
        Ties are broken with the smaller end
        Pop from the top of the heap, update current capacity
        Add the top to a heap with smallest end on top
        If the next top of the start heap is greater than the end of the end heap
            then pop from the end heap and decrement the current capacity
        """
        
        # (start, end, num_passengers)
        start_heap = list(map(lambda t: (t[1], t[2], t[0]), trips))
        heapq.heapify(start_heap)
        
        # (end, start, num_passengers)
        end_heap = []
        
        cur_cap = 0
        
        # Iterate through all trips
        while start_heap:
            top_start, top_end, top_num_pass = heapq.heappop(start_heap)
            
            # Pop all trips that have ended from the end heap
            while end_heap and end_heap[0][0] <= top_start:
                end, start, num_pass = heapq.heappop(end_heap)
                cur_cap -= num_pass
            
            # Update car capacity and break if necessary
            cur_cap += top_num_pass
            if cur_cap > capacity:
                return False
            
            # Add the new trip to the end heap
            heapq.heappush(end_heap, (top_end, top_start, top_num_pass))

        
        # If all trips could be completed, we return True
        return True

