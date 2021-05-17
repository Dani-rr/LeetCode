class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        output = 0
        for i in s:
            if i == 'L':
                l += 1
            elif i == 'R':
                r += 1
            if l == r:
                output += 1
                l = 0
                r = 0
        return output