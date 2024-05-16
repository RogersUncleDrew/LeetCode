class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0]==0:
                for j in range(n):
                    grid[i][j] = 1- grid[i][j]
        mul = [2 ** j for j in range(n-1, -1, -1)]
        ans = 0
        for j in range(n):
            count = {0:0, 1:0}
            for i in range(m):
                count[grid[i][j]]+=1
            ans += max(count[0], count[1]) * mul[j]
        return ans
