class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        n = len(points)
        r = points[0][1]
        ans = 1
        for i in range(1, n):
            if points[i][0]>r:
                r = points[i][1]
                ans += 1
            else:
                r = min(r, points[i][1])
        return ans
