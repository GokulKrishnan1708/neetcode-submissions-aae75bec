class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(groupSize):
                if count[first + i] == 0:
                    return False
                count[first + i] -= 1
                if count[first + i] == 0:
                    if first + i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True