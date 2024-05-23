class Solution:
    def knightDialer(self, n: int) -> int:
        nextNum = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        @cache
        def dfs(i,n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            ans = 0
            for nextI in nextNum[i]:
                ans += dfs(nextI, n-1)%(10 ** 9 + 7)
            return ans%(10 ** 9 + 7)
        ans = 0
        for i in range(10):
            ans += dfs(i,n)%(10 ** 9 + 7)
        return ans % (10 ** 9 + 7)
