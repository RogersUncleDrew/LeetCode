class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        upper = max(nums)
        mod = 10**9 + 7
        cnt = [0 for _ in range(upper + 1)]
        pre = [0 for _ in range(upper + 1)]
        for i in nums:
            cnt[i]+=1
        for i in range(1, upper + 1):
            pre[i] = pre[i-1] + cnt[i]
        ans= 0
        for i in range(1, upper + 1):
            if cnt[i]:
                d = 1
                while d*i<=upper:
                    ans+=cnt[i] * d *(pre[min((d+1)*i-1, upper)]-pre[d*i-1])
                    d+=1
        return ans % mod

