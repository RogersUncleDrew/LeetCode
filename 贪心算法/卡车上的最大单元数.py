class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        n = len(boxTypes)
        i = 0
        ans = 0
        while truckSize > 0 and i<n:
            numOfi = min(truckSize, boxTypes[i][0])

            ans += numOfi * boxTypes[i][1]
            if numOfi == boxTypes[i][0]:
                i += 1
            truckSize -= numOfi
        return ans
