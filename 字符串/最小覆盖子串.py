class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        ans = [0, float("inf")]
        num = len(t)
        for i in t:
            count[i] += 1
        l = 0
        for r, x in enumerate(s):
            if count[x] > 0:
                num -= 1
            count[x] -= 1
            if num == 0:
                while True:
                    c = s[l]
                    if count[c] == 0:
                        break
                    l += 1
                    count[c] += 1
                if r - l < (ans[1] - ans[0]):
                    ans = [l, r]
                num += 1
                count[c] += 1
                l += 1
        return "" if ans[1]>len(s) else s[ans[0]:ans[1]+1]
                
