class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k>n:
            return False
        count = Counter(s)
        ji = 0
        for i in count:
            if count[i]%2==1:
                ji+=1
        return ji <= k
