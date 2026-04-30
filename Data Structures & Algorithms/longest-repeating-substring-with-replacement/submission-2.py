class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        left = 0
        n = len(s)
        res = 0
        for right in range(n):
            check[s[right]] = check.get(s[right] , 0) + 1
            while (right - left + 1) - check[max(check, key=check.get)] > k:
                check[s[left]] = check.get(s[left] , 1) - 1
                left += 1
            res = max(res, right - left + 1)
        return res

        