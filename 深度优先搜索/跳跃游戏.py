class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False for i in range(n)]

        def dfs(start):
            if visited[start]:
                return False
            if arr[start] == 0:
                return True
            visited[start] = True
            returnV = False
            for i in [start - arr[start], n - 1, start + arr[start]]:
                if 0<=i <n:
                    returnV = returnV or dfs(i)
            visited[start] = False
            return returnV

        return dfs(start)
