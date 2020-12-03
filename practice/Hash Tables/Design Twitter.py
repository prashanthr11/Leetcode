from collections import defaultdict as dt
from collections import deque as dq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = dt(list)
        self.posts = dt(dq)
        self.newsfeed = dt(dq)
        self.cnt = 0
        

    def postTweet(self, id: int, tweet: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[id].appendleft((self.cnt, tweet))
        self.cnt += 1
        

    def getNewsFeed(self, id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ret = list()
        tmp = self.posts[id]
        if tmp:
            for i in tmp:
                ret.append(i)
        
        for i in self.follows[id]:
            for j in self.posts[i]:
                ret.append(j)

        ret.sort(reverse = True)#, key = lambda x:x[0])
        res = list()
        
        for i in ret[:10]:
            if len(i):
                res.append(i[1])
            
        return res
        

    def follow(self, id: int, followee: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if id != followee and followee not in self.follows[id]:
            self.follows[id].append(followee)

    def unfollow(self, id: int, followee: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if id != followee and followee in self.follows[id]:
                self.follows[id].remove(followee)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
