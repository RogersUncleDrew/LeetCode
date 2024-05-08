class ProductOfNumbers:

    def __init__(self):
        self.preMul = [1]


    def add(self, num: int) -> None:
        if num == 0:
            self.preMul = [1]
        else:
            self.preMul.append(self.preMul[-1]*num)


    def getProduct(self, k: int) -> int:
        if k>=len(self.preMul):
            return 0
        else:
            return self.preMul[-1]//self.preMul[-1-k]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
