class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_s, len_w, len_p = len(s), len(words), len(words[0])
        ans = []
        for i in range(len_p):
            if i + len_w * len_p > len_s:
                break
            count = Counter()
            for j in range(i, i + len_w * len_p, len_p):
                word = s[j:j + len_p]
                count[word] += 1
            for word in words:
                count[word] -= 1
                if count[word] == 0:
                    del count[word]
            if len(count) == 0:
                ans.append(i)
            for start in range(i, len_s - len_p * len_w, len_p):
                if start + len_p * len_w + len_p > len_s:
                    break
                word_left = s[start:start + len_p]
                count[word_left] -= 1
                if count[word_left] == 0:
                    del count[word_left]
                word_right = s[start + len_p * len_w : start + len_p * len_w + len_p]
                count[word_right] += 1
                if count[word_right] == 0:
                    del count[word_right]
                if len(count) == 0:
                    ans.append(start + len_p)
        return ans
