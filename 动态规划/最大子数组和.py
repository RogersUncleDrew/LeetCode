class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = 0
        ans = -float("inf")
        for i in range(1, n+1):
            f = max(0, f) + nums[i-1]
            ans = max(ans, f)
        return ans
