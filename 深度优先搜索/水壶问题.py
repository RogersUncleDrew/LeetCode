class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = defaultdict(bool)
        def dfs(i,j):
            if visited[i,j]:
                return False
            visited[i,j] = True
            if i+j == target:
                return True
            if x-i<=j:
                p1,q1 = x, j-(x-i)
            else:
                p1, q1 = i+j, 0
            if y-j <= i:
                p2, q2 = i - (y - j), y
            else:
                p2, q2 = i + j, 0
            return dfs(x,j) or dfs(i,y) or dfs(0,j) or dfs(i,0) or dfs(p1, q1) or dfs(p2, q2)
        return dfs(0, 0)
