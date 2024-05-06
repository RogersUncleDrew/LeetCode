class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length()-1
        self.parent = [[parent[i]] + [-1 for _ in range(m)] for i in range(n)]
        for x in range(m):
            for i in range(n):
                p = self.parent[i][x]
                if p!=-1:
                    self.parent[i][x+1] = self.parent[p][x]


            


    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 的二进制从低到高第 i 位是 1
                node = self.parent[node][i]
                if node < 0: break
        return node





# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
