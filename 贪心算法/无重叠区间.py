class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        l, r = intervals[0][0], intervals[0][1]
        ans = 1
        for i in range(1, n):
            if intervals[i][0] >= r:
                r = intervals[i][1]
                ans += 1
            else:
                r = min(r, intervals[i][1])
        return n - ans
