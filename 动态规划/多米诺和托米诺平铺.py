class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c, d = 0, 0, 0, 1
        for i in range(1, n + 1):
            a, b, c, d = d, a + c, a + b, a + b + c + d
        return d % (10**9 + 7)
