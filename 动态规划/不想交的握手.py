class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = [0 for i in range(numPeople + 1)]
        dp[0] = 1
        for i in range(2, numPeople+2, 2):
            for j in range(2, i + 1, 2):
                dp[i] += dp[i-j] * dp[j-2]
        return dp[numPeople] % (10**9+7)
