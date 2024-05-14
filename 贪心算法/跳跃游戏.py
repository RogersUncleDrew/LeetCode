class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        now = 0
        i = 0
        while i < n:
            if i > now:
                return False
            now = max(now, i + nums[i])
            if now >= n - 1:
                return True
            i += 1
        return False
