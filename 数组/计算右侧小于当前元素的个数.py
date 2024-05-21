class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        n = len(nums)
        res = [0 for i in range(n)]
        sl = SortedList()
        for i in range(n-1, -1, -1):
            cnt = sl.bisect_left(nums[i])
            res[i] = cnt
            sl.add(nums[i])
        return res
