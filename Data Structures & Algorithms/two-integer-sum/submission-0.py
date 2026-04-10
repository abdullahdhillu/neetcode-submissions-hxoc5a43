class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set1 = {}
        for i, x in enumerate(nums):
            if target - x not in set1:
                set1[x] = i
            else:
                return [set1[target - x], i]
        return [-1, -1]