from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.tweets:
            feed.extend(self.tweets[userId])
        if userId in self.follows:
            for followee in self.follows[userId]:
                if followee in self.tweets:
                    feed.extend(self.tweets[followee])
        return [tweetId for _, tweetId in heapq.nlargest(10, feed, key=lambda x: x[0])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
