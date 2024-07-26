class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        count = [0 for i in range(26)]
        maxC, maxN = 0, 0
        for i in tasks:
            count[ord(i) - ord("A")] += 1
            maxC = max(maxC, count[ord(i) - ord("A")])
        for i in range(26):
            maxN += 1 if count[i] == maxC else 0
        return max(m, (maxC - 1) * (n +1) + maxN)
