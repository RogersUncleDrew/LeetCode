class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i==")" and stack and stack[-1] == "(":
                stack.pop()
                continue
            stack.append(i)
        return len(stack)
