class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0 for _ in range(26)]]
        for i in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(i) - ord("a")]+=1
        ans = []
        for l, r, k in queries:
            m = 0
            for sl, sr in zip(sum[l], sum[r + 1]):
                m += (sr - sl) % 2
            ans.append(m // 2 <= k)
        return ans
