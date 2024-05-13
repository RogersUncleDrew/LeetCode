class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dpMin = 0
        dpMax = -float("inf")
        fMin = 0
        fMax = -float("inf")
        ans = 0
        total = sum(nums)
        for i in range(1, n + 1):
            dpMin = min(0, dpMin) + nums[i-1]
            dpMax = max(0, dpMax) + nums[i-1]
            fMin = min(fMin, dpMin)
            fMax = max(fMax, dpMax)
        return max(fMax, total-fMin) if fMin != total else fMax
