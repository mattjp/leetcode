class Leaderboard:

    def __init__(self):
        # map playerId to mostRecentHighScore
        self.scores = {}
        
        # keep PQ of (score, playerId)
        self.top_scores = []
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score
        heapq.heappush(self.top_scores, (-self.scores[playerId], playerId))
        

    def top(self, K: int) -> int:
        output, count = 0, 0
        valid_scores = []
        while count < K and self.top_scores:
            score, player_id = heapq.heappop(self.top_scores)
            if self.scores[player_id] == -score:
                output += score
                count += 1
                valid_scores.append([score, player_id])
                
        for vs in valid_scores:
            heapq.heappush(self.top_scores, (vs[0], vs[1]))
            
        return -output
        

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] = 0
            heapq.heappush(self.top_scores, (0, playerId))
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
