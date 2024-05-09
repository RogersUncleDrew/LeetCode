class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minV, maxV = 2, 2 * limit
        count = [0 for i in range(maxV + 2)]
        for i in range(n // 2):
            a, b = nums[i], nums[-1 - i]
            a, b = min(a, b), max(a, b)
            count[2] += 2
            count[1 + a] -= 1
            count[a + b] -= 1
            count[a + b + 1] += 1
            count[b + limit + 1] += 1
        for i in range(minV, maxV + 1):
            count[i] += count[i - 1]
        return min(count[minV:maxV+1])
