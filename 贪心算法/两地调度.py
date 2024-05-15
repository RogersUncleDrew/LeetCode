class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x:x[0]-x[1])
        ans = 0
        return sum(i for i, j in costs[:n//2]) + sum(j for i,j in costs[n//2:])
