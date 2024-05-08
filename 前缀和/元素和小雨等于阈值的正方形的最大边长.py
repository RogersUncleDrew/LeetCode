class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        self.pre = [[0 for i in range(n + 1)] for j in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre[i][j] = self.pre[i][j - 1] + self.pre[i - 1][j] - self.pre[i - 1][j - 1] + mat[i - 1][j - 1]

        def check(d):
            for i in range(d, m + 1):
                for j in range(d, n + 1):
                    square = self.pre[i][j] + self.pre[i - d][j - d] - self.pre[i ][j - d] - self.pre[i - d][j]
                    if square <= threshold:
                        return True

            return False

        l, r = 1, min(m, n)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
