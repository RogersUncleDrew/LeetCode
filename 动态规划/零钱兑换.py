class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in coins:
            if i<=amount:
                dp[i] = 1
        for j in coins:
            for i in range(1, amount+1):
                if i>=j:
                    dp[i] = min(dp[i-j] + 1, dp[i])
        return dp[amount] if dp[amount]!=float("inf") else -1
