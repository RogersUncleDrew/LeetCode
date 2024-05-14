class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            change = i - 5
            if change > 0:
                needTen = min(change // 10, ten)
                change -= needTen * 10
                ten -= needTen
                needFive = change // 5
                if needFive > five:
                    return False
                else:
                    five -= needFive

            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
        return True
