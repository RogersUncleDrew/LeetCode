class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        pre = nums[0]
        res = nums[0]
        q = [(0, nums[0])]
        for i in range(1, 2*n):
            while q and i - q[0][0] > n:
                q.pop(0)
            pre += nums[i%n]
            res = max(res, pre - q[0][1])
            while q and q[-1][1] >= pre:
                q.pop()
            q.append((i, pre))
        return res
