class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        flag = False
        for i in range(n-1):
            flag = True
            j = i
            for j in range(n - 1 - i):
                if nums[j+1] <= nums[j]:
                    nums[j] , nums[j+1] = nums[j+1], nums[j]    
                    flag = True
                j += 1
            if not flag:
                return nums
        return nums

        