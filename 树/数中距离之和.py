class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        length = [0 for i in range(n)]
        size = [1 for i in range(n)]
        connect = [[] for i in range(n)]
        for x,y in edges:
            connect[x].append(y)
            connect[y].append(x)
        def dfs1(x, parent, depth):
            length[0] += depth
            for i in connect[x]:
                if i!=parent:
                    size[x] += dfs1(i, x, depth + 1)
            return size[x]
        dfs1(0, -1, 0)
        def dfs2(x, parent):
            for i in connect[x]:
                if i!= parent:
                    length[i] = length[x] + n - 2*size[i]
                    dfs2(i, x)
        dfs2(0, -1)
        return length
