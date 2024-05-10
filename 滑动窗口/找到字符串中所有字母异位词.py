class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s<len_p:
            return []
        ans = []
        count = [0 for i in range(26)] #记录s比p多的字母的个数
        for i in range(len_p):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(p[i]) - ord("a")] -= 1
        differ = [i != 0 for i in count].count(True)
        if differ == 0:
            ans.append(0)
        for i in range(len_s - len_p):
            if count[ord(s[i]) - ord("a")] == 1:
                differ -= 1
            elif count[ord(s[i]) - ord("a")] == 0:
                differ += 1
            count[ord(s[i]) - ord("a")] -= 1

            if count[ord(s[i + len_p]) - ord("a")] == -1:#如果本来s[i+len_p]这个字母在s中比这字母在p中少一个
                differ -= 1
            elif count[ord(s[i + len_p]) - ord("a")] == 0:
                differ += 1
            count[ord(s[i + len_p]) - ord("a")] += 1
            if differ == 0:
                ans.append(i + 1)
        return ans
