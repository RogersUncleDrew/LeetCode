class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        way = [[0 for j in range(n)] for i in range(m)]
        if m<=1 or n<=1:
            return 1
        for i in range(m):
            way[i][0] = 1
        for i in range(n):
            way[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                way[i][j] = way[i-1][j]+way[i][j-1]

        return way[m-1][n-1]
