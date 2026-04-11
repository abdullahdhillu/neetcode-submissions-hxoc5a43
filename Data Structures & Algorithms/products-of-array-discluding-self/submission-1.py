class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums) 
        temp1 ,temp2 = 1, 1
        for i in range(len(nums)):
            temp1 *= nums[i]
            prefix[i] = temp1
        for i in range(len(nums) - 1, -1 , -1):
            temp2 *= nums[i]
            suffix[i] = temp2
        res = []
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums) - 1 else 1
            res.append(left*right)
        return res
           