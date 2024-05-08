class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        pre = [0 for i in range(n)]
        suf = [0 for i in range(n)]
        for i in range(1, n):
            pre[i] = pre[i-1] + (1 if s[i-1]=="1" else 0)
        for j in range(n-2, -1, -1):
            suf[j] = suf[j+1] + (1 if s[j+1]=="0" else 0)
        return min([pre[i] + suf[i] for i in range(n)])
