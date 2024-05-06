class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        graph = defaultdict(list)
        for i in regions:
            graph[i[0]] = i[1:]
        self.ans = ""
        def dfs(place):
            returnV = False
            count = 0
            if place == region1 or place == region2:
                returnV = True
                count+=1
            if place in graph:
                for child in graph[place]:
                    if dfs(child):
                        count+=1
                        returnV = True
                if count>=2:
                    self.ans = place
                return returnV
            return returnV
        dfs(regions[0][0])
        return self.ans
