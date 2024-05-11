class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        nums = [0] + nums + [0]
        n = len(nums)
        right_first_smaller = [None for i in range(n)]
        left_first_smaller = [None for i in range(n)]
        stack =[]
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                right_first_smaller[stack.pop()] = i
            stack.append(i)
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                left_first_smaller[stack.pop()] = i
            stack.append(i)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        res = 0
        for i in range(1, n-1):
            left = left_first_smaller[i]
            right = right_first_smaller[i]
            res = max(res, nums[i] * (pre[right] -pre[left+1]))
        return res % mod
