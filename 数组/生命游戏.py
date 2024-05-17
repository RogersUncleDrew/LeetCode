class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live_neighbour = 0
                for r, c in direction:
                    x, y = i + r, j + c
                    if 0 <= x < m and 0 <= y < n and (board[x][y] == 1 or board[x][y] == 2):
                        live_neighbour += 1
                if board[i][j] == 1:
                    if live_neighbour < 2 or live_neighbour > 3:
                        board[i][j] = 2  # 活到死
                elif board[i][j] == 0:
                    if live_neighbour == 3:
                        board[i][j] = 3  # 死到活
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
