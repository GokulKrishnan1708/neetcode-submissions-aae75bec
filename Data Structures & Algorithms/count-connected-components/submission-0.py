class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for a, b in edges:
            union(a, b)

        return len(set(find(x) for x in range(n)))