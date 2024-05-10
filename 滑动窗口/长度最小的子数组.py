class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        n = len(nums)
        curSum = 0
        l, r = 0, 0
        while l < n:
            while curSum < target and r < n:
                curSum += nums[r]
                r += 1
            while curSum >= target and l <= r:
                length = r - l
                ans = min(ans, length)
                curSum -= nums[l]
                l += 1
            if r == n:
                break
        return ans if ans!= float("inf") else 0
