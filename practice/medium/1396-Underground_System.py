class UndergroundSystem:

    def __init__(self):
        # map startStation-endStation => (sum, count)
        self.times = {}
        # map riderId => (startStation, startTime)
        self.riders = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.riders:
            self.riders[id] = (stationName, t)
            

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.riders:
            start_station, u = self.riders[id]
            time_id = start_station + '-' + stationName
            prev_sum, prev_count = 0, 0
            if time_id in self.times:
                prev_sum, prev_count = self.times[time_id]
            time = t - u
            self.times[time_id] = (prev_sum + time, prev_count + 1)
            del self.riders[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_id = startStation + '-' + endStation
        time_sum, count = self.times[time_id]
        return time_sum / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
