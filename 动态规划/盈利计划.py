class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(minProfit + 1)] for i in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1
        for x,y in zip(group, profit):
            for m in range(n, x-1, -1):
                for p in range(minProfit, -1, -1):
                    dp[m][p] = (dp[m][p] + dp[m-x][max(0, p-y)]) % MOD
        return dp[-1][-1]
