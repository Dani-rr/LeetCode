class Solution:
    def kWeakestRows(self, mat, k):
        lst_1 = mat
        output = []
        for i in range(k):
            aa = lst_1.index(max(sum(lst_1.reverse())))
            output.append(aa)
            lst_1.pop(aa)
        return output

test = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

Solution().kWeakestRows(test, 3)


test = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
lst_1.index(max(sum(test.reverse())))