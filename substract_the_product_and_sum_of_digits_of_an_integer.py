class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        sume = 0
        product = 1
        for i in string:
            sume += int(i)
            product = product * int(i)
        output = product - sume
        return output