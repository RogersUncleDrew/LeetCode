class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for i in range(n)]
        for l,r,p in bookings:
            ans[l-1] += p
            if r<n:
                ans[r]-=p
        for i in range(1, n):
            ans[i]+=ans[i-1]
        return ans
