class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = list()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        ans = [queue[0]]
        for i in range(k, n):
            if nums[i - k] == queue[0]:
                queue.pop(0)
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            ans.append(queue[0])
        return ans
