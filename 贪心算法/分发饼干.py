class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        len_g, len_s = len(g), len(s)
        point_g, point_s = 0, 0
        ans = 0
        while point_g < len_g and point_s < len_s:
            if s[point_s] >= g[point_g]:
                ans += 1
                point_s += 1
                point_g += 1
            else:
                point_s += 1
        return ans
