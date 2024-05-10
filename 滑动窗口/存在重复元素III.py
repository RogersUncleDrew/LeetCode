from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i >indexDiff:
                window.remove(nums[i-1-indexDiff])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])#找到比nums[i]所在的索引
            if idx!=0 and abs(nums[i] - window[idx - 1])<=valueDiff:
                return True
            if idx!=len(window) - 1 and abs(nums[i] - window[idx + 1])<= valueDiff:
                return True
        return False
