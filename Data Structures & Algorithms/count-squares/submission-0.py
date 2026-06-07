from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (px, py), cnt in self.points.items():
            if abs(px - x) == 0 or abs(px - x) != abs(py - y):
                continue
            res += cnt * self.points.get((px, y), 0) * self.points.get((x, py), 0)
        return res
