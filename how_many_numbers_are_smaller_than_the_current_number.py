class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            n = 0
            for j in nums:
                if i > j:
                    n += 1
            output.append(n)
        return output