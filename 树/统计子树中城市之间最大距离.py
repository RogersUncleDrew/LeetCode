class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        connect = defaultdict(list)
        for x, y in edges:
            connect[x - 1].append(y - 1)
            connect[y - 1].append(x - 1)
        ans = [0 for i in range(n - 1)]
        inset = [False for i in range(n)]
        def subSet(i):
            inset[i] = True
            diameter = 0
            far = i
            visited = [False for _ in range(n)]
            def dfs(x, par, currentLength):
                nonlocal far
                nonlocal diameter
                visited[x] = True
                if currentLength > diameter:
                    far = x
                    diameter = currentLength
                for y in connect[x]:
                    if y != par and inset[y]:
                        dfs(y, x, currentLength + 1)
            dfs(i, -1, 0)
            diameter = 0
            visited = [False for _ in range(n)]
            dfs(far, -1, 0)
            if diameter and visited == inset:
                ans[diameter - 1] += 1
            for j in range(i + 1, n):
                subSet(j)
            inset[i] = False
        for i in range(n):
            subSet(i)
        return ans
