class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = [[] for _ in range(len(nums) + 1)]
        ans = []
        for x in nums:
            dict[x] = dict.get(x, 0) + 1
        for key, value in dict.items():
            res[value].append(key)
        for x in range(len(nums), 0 , -1):
            for n in res[x]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        