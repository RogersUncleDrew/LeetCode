class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]
        dp1[0] = nums[0]
        for i in range(1, n):
            dp1[i] = dp2[i-1] + nums[i]
            dp2[i] = max(dp2[i-1], dp1[i-1])
        return max(dp1[n-1], dp2[n-1])
