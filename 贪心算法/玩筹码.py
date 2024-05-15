class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ji = 0
        ou = 0
        for i in position:
            if i%2==1:
                ji+=1
            else:
                ou+=1
        return min(ji, ou)
