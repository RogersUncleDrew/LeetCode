class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a,b = 0,0
        n = len(s1)
        for i in range(n):
            if s1[i]=="x" and s2[i] == "y":
                a+=1
            elif s1[i] == "y" and s2[i] == "x":
                b+=1
        if (a+b)%2==1:
            return -1
        return (a+b)//2 + a%2
