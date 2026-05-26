class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries_sorted = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)
        heap = []
        j = 0

        for q, i in queries_sorted:
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(heap, (r - l + 1, r))
                j += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]

        return res