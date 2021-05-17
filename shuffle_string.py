class Solution:
    def restoreString(self, s, indices):
        dct = {}
        output = ''
        for i, j in zip(s, indices):
            dct[j] = i
        for k in sorted(dct):
            output += dct[k]
        return output
