class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.map = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.map[i][j] = self.map[i-1][j] + self.map[i][j-1] + matrix[i-1][j-1] - self.map[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.map[row2 + 1][col2 + 1] + self.map[row1][col1] - self.map[row1][col2+1] - self.map[row2+1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
