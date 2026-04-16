class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for word in words:
            for char in word:
                indegree[char] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while queue:
            c = queue.popleft()
            res.append(c)
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(res) < len(indegree):
            return ""
        return "".join(res)