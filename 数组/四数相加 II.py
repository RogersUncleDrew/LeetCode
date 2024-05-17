class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        index = defaultdict(int)
        for i,x in enumerate(nums1):
            for j,y in enumerate(nums2):
                index[x+y]+=1
        for i,x in enumerate(nums3):
            for j,y in enumerate(nums4):
                temp = -(x+y)
                if temp in index:
                    ans+=index[temp]
        return ans
