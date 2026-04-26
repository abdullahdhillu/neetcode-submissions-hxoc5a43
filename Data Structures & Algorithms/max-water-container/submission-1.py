class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        i , j = 0 , n - 1
        while i < j:
            weight = (j - i) * min(heights[j] , heights[i])
            res = max(res, weight)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res
