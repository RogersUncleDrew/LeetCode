class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        self.pre = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            self.pre[i] = self.pre[i - 1] ^ arr[i - 1]
        for l in range(n):
            for r in range(l + 1, n + 1):
                if self.pre[l] == self.pre[r]:
                    ans += (r - l - 1)
        return ans
