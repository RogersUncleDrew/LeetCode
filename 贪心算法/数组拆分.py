class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        i = 0
        while i<n:
            ans += nums[i]
            i+=2
        return ans
