class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curMul = 1
        i = 0
        ans = 0
        for j,x in enumerate(nums):
            curMul *= x
            while i<=j and curMul>=k:
                curMul //= nums[i]
                i+=1
            ans+=(j-i+1)
        return ans

                    

            
