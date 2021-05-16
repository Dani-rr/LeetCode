class Solution:
    def numIdenticalPairs(self, nums):
        for i in range(len(nums)):
            for v1 in nums[i+1:]:
                if v1 == nums[i]:
                    n += 1
        return n
