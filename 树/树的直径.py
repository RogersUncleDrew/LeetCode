class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        connect = defaultdict(list)
        for x, y in edges:
            connect[x].append(y)
            connect[y].append(x)
        self.far = 0
        self.len = 0
        def dfs(x, parent, curLen):
            if curLen > self.len:
                self.far = x
                self.len = curLen
            for i in connect[x]:
                if i != parent:
                    dfs(i, x, curLen + 1)
        dfs(0, -1, 0)
        self.len = 0
        dfs(self.far, -1, 0)
        return self.len
