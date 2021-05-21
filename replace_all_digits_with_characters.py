class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ''
        for i, j in zip (s, s[1:]):
            if i.isnumeric():
                continue
            else:
                output += i
                new = chr(int(ord(i)) + int(j))
                output += new
        if s[-1].isalpha():
            output += s[-1]
        return output
