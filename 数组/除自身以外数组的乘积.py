class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for i in range(n)]
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        mul = 1
        for i in range(n-2, -1, -1):
            mul*=nums[i+1]
            ans[i] = ans[i]*mul
        return ans
