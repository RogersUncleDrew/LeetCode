class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l,r = 0,0
        while r<n:
            while r<n and nums[r] == 0:
                r+=1
            if r< n:
                nums[l] = nums[r]
                l+=1
            r+=1
        for i in range(l, n):
            nums[i] = 0
