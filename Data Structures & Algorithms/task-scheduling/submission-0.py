class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        countMax = sum(1 for v in freq.values() if v == maxFreq)
        
        partCount = (maxFreq - 1) * (n + 1) + countMax
        return max(partCount, len(tasks))