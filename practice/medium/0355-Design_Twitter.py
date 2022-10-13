from collections import defaultdict

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)  # keyId follows all valIds
        self.tweets = defaultdict(list)  # list of chronological tweets per user
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1
        
        
    def getMostRecentTweets(self, userId):
        return self.tweets[userId][-10:]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        recent = []
        followees = self.follows[userId]
        followees.add(userId)  # show the users tweets to themself
        
        # get the 10 most recent tweets for all accounts that the user follows
        for fid in followees:
            recent.extend(self.getMostRecentTweets(fid))
            
        # turn into a heap sorted by timestamp
        heapq.heapify(recent)
        
        # keep the 10 most recent tweets
        feed = heapq.nlargest(10, recent)
        return [tid for ts, tid in feed]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:        
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
