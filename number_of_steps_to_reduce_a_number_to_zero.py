class Solution:
    def numberOfSteps(self, num: int) -> int:
        output = 0
        while num > 0:
            if num%2 == 0:
                num = num/2
                output += 1
            else:
                num -= 1
                output += 1
        return output
