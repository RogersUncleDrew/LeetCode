class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp = [0 for i in range(target+1)]
        for i in range(n):
            for j in range(target, -1, -1):
                if j >= stones[i]:
                    dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return total - 2 * dp[-1]
