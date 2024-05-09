class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max([trips[i][-1] for i in range(len(trips))])
        nums = [0 for i in range(n+1)]
        for p,l,r in trips:
            nums[l]+=p
            nums[r]-=p
        if nums[0]>capacity:
            return False
        for i in range(1, n+1):
            nums[i] += nums[i-1]
            if nums[i]>capacity:
                return False
        return True
