class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1 or total < target or target < -total:
            return 0
        obj = (total + target) // 2
        dp = [0 for i in range(obj + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(obj, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]
