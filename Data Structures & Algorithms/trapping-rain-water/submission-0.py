class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        maxLeft = []
        curr_max = height[0]
        for i in height:
            curr_max = max(curr_max , i)
            maxLeft.append(curr_max)
        n = len(height)
        maxRight = []
        curr_max = height[n-1]
        for i in range(n - 1, -1, -1):
            curr_max = max(curr_max, height[i])
            maxRight.append(curr_max)
        maxRight.reverse()
        for i in range(n):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                ans += water
        return ans
