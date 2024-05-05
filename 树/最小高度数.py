class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        connect = defaultdict(list)
        for x, y in edges:
            connect[x].append(y)
            connect[y].append(x)
        self.far = 0
        self.len = 0
        parent = [-1 for i in range(n)]

        def dfs(x, par, curLen):
            if curLen > self.len:
                self.far = x
                self.len = curLen
            parent[x] = par
            for i in connect[x]:
                if i != par:
                    self.path.append(i)
                    dfs(i, x, curLen + 1)
                    self.path.pop()

        self.path = [0]
        dfs(0, -1, 0)
        self.len = 0
        dfs(self.far, -1, 0)
        self.longestPath = []
        while self.far != -1:
            self.longestPath.append(self.far)
            self.far = parent[self.far]


        v = len(self.longestPath)
        if v % 2 == 0:
            return [self.longestPath[v//2-1], self.longestPath[v//2]]
        else:
            return [self.longestPath[v//2]]
