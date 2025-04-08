class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        c1, d1 = points.pop()
        while points:
            c2, d2 = points.pop()
            res += max(abs(d2 - d1), abs(c2 - c1))
            c1, d1 = c2, d2;
        return res