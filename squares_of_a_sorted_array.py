class Solution:
    def sortedSquares(self, nums):
        output = []
        for i in nums:
            output.append(i**2)
        return sorted(output)


nums = [-4,-1,0,3,10]
Solution().sortedSquares(nums)