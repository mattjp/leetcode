class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # Sort stations by distance from start, 0
        heapq.heapify(stations)
        
        # We start with an empty tank at distance 0
        tank = 0
        dist = 0
        ans = 0
        
        # We treat the first station as dist=0, fuel=startFuel
        # Use a heap to greedily select the max fuel seen at a station so far
        pq = [-startFuel]
        
        while pq:
            fuel = heapq.heappop(pq) * -1
            dist += fuel
            
            if dist >= target:
                return ans
            
            # We've had to visit 1 additional station
            ans += 1
            
            # Add all of the possible stations to the PQ
            while stations and stations[0][0] <= dist:
                d, f = heapq.heappop(stations)
                heapq.heappush(pq, -f)
                
        return -1
