class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        def change(list_n):
            num = len(list_n)
            for i in range(1, num):
                if int(list_n[i]) < int(list_n[i-1]):
                    for j in range(i, num):
                        list_n[j] = "9"
                    list_n[i-1] = str(int(list_n[i-1]) - 1)
                    list_n[:i] = change(list_n[:i])
            return list_n
        list_n = list(str(n))
        list_n = change(list_n)
        return int("".join(list_n).lstrip('0') or "0")
