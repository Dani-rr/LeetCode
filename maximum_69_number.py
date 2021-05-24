class Solution:
    def maximum69Number(self, num):
        output = ''
        changes = 0
        for i in str(num):
            if changes == 0:
                if i == '6':
                    output += '9'
                    changes += 1
                else:
                    output += i
            else:
                output += i
        return int(output)
