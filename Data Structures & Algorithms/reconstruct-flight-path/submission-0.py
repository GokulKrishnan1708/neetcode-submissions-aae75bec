class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        route = []
        def dfs(airport):
            while graph[airport]:
                dfs(heapq.heappop(graph[airport]))
            route.append(airport)
        dfs("JFK")
        return route[::-1]
