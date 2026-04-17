class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        heap = [(0, src, 0)]
        dist = {}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k or (node in dist and dist[node] < stops):
                continue
            dist[node] = stops
            if node in graph:
                for nei, price in graph[node]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))
        
        return -1