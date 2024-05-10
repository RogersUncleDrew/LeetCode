from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        ans = []
        for i in range(k):
            window.add(nums[i])
        if k%2 ==1:
            ans.append(window[k//2])
        else:
            ans.append((window[k//2-1] + window[k//2])/2)
        for i in range(k,len(nums)):
            window.add(nums[i])
            window.remove(nums[i-k])
            if k%2 ==1:
                ans.append(window[k//2])
            else:
                ans.append((window[k//2-1] + window[k//2])/2)
        return ans
