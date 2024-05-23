class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        index= {(i,j):1 for i in range(m) for j in range(n)}
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    index[i,j] = 1
                elif i==0:
                    index[i,j] = index[i,j-1]
                elif j==0:
                    index[i,j] = index[i-1,j]
                else:
                    index[i,j] = index[i-1,j] +  index[i, j-1]
                if obstacleGrid[i][j]==1:
                    index[i,j] = 0
        return index[m-1, n-1]
