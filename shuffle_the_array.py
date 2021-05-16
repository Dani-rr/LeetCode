class Solution:
    def shuffle(self, nums, n):
        output = []
        for i,j in zip(nums[:n+1], nums[n:]):
            output.append(i)
            output.append(j)
        return output

print(1)