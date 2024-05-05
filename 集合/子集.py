class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)
        visited = [False for i in range(n)]
        def dfs(i, path):
            ans.append(path+[nums[i]])
            for j in range(i+1,n):
                dfs(j, path + [nums[i]])
        for i in range(n):
            dfs(i, [])
        return ans
