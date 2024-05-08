class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preMul = [1 for i in range(n)]
        sufMul = [1 for i in range(n)]
        for i in range(1, n):
            preMul[i] = preMul[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            sufMul[i] = sufMul[i+1] * nums[i+1]
        return [preMul[i] * sufMul[i] for i in range(n)]
