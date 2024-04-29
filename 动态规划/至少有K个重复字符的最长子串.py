class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(l, r, k):
            if r - l + 1 < k:
                return 0
            index = defaultdict(int)
            for i in range(l, r + 1):
                index[s[i]] += 1
            while r - l + 1 >= k and index[s[l]] < k:
                l += 1
            while r - l + 1 >= k and index[s[r]] < k:
                r -= 1
            for i in range(l, r + 1):
                if index[s[i]] < k:
                    return max(dfs(l, i - 1, k), dfs(i + 1, r, k))
            return r - l + 1
        return dfs(0,len(s)-1, k)
