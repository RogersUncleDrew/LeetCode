class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profitList = [prices[i] - prices[i-1] for i in range(1, n)]
        ans = 0
        for i in profitList:
            if i>0:
                ans +=i
        return ans
