class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.str = ""

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
        node.str = word


class Solution:
    def findWords(self, board, words):
        self.trie =Trie()
        for word in words:
            self.trie.insert(word)
        m,n = len(board), len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        returnList = set()
        def dfs(i, j, node):
            visited[i][j] = True
            if board[i][j] not in node.children:
                visited[i][j] = False
                return
            node=node.children[board[i][j]]
            if node.isEnd:
                returnList.add(node.str)
            for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    dfs(x,y,node)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                dfs(i,j,self.trie)
        return list(returnList)
