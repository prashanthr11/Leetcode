from collections import defaultdict as dt

class UndergroundSystem:

    def __init__(self):
        self.passenger = dt(list)
        self.time = dt(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        previous_station, dep = self.passenger[id]
        self.time[(previous_station, stationName)].append(t - dep)

    def getAverageTime(self, start: str, end: str) -> float:
        total = self.time[(start, end)]
        
        return sum(total)/len(total)
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
