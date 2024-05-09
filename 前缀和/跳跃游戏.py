class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0 for i in range(n)]
        dp[0] = 1
        pre = [0 for i in range(n)]
        for i in range(minJump):
            pre[i] = 1
        for i in range(minJump, n):
            if s[i] == "0":
                left, right = i-maxJump, i - minJump
                total = pre[right] - (pre[left - 1] if left > 0 else 0)
                if total > 0:
                    dp[i] = 1
            pre[i] = pre[i-1] + dp[i]
        return dp[n - 1] == 1
