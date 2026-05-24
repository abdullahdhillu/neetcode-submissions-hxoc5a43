class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dick = dict()
        n = len(nums)
        for num in nums:
            dick[num] = dick.get(num, 0) + 1
        max = 0
        res = 0
        for key, value in dick.items():
            if value > max:
                max = value
                res = key
        return res
        