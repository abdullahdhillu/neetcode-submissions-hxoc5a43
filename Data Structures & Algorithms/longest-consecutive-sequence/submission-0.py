class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maps = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in maps:
                length = 0
                while n + length in maps:
                    length += 1
                longest = max(longest, length)
        return longest