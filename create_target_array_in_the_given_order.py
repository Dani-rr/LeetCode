class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, j in zip(nums, index):
            if j >= len(target):
                target.append(i)
            else:
                target.insert(j, i)
        return target