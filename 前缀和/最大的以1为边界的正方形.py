class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        pre_r = [list(accumulate(row, initial=0)) for row in grid]  # 每行的前缀和
        pre_c = [list(accumulate(col, initial=0)) for col in zip(*grid)]  # 每列的前缀和
        for d in range(min(m, n), 0, -1):
            for i in range(m-d+1):
                for j in range(n-d+1):
                    if pre_r[i][j+d] - pre_r[i][j] == d and \
                    pre_c[j][i+d] - pre_c[j][i] == d and\
                    pre_r[i+d-1][j+d] - pre_r[i+d-1][j] == d and \
                    pre_c[j+d-1][i+d] - pre_c[j+d-1][i] == d:
                        return d*d
        return 0
