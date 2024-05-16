class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        i = 0
        leftNum = n- k
        while i < n:
            int_i = int(num[i])
            while stack and stack[-1] > int_i and k > 0:
                stack.pop()
                k -= 1
            stack.append(int_i)
            i += 1
        stack = [str(i) for i in stack[:leftNum]]
        return "".join(stack).lstrip('0') or "0"
