class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                res.append(size)
                size = 0
        return res