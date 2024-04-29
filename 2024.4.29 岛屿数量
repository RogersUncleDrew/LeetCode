class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n =len(grid), len(grid[0])
        def dfs(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for (x,y) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0<=x<m and 0<=y<n:
                        dfs(x, y)
            else:
                return
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans+=1
                    dfs(i,j)
        return ans
