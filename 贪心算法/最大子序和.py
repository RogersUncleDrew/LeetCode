class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, temp = -float("inf"), 0
        for i in nums:
            temp = max(temp, 0) + i
            ans = max(ans, temp)
        return ans
