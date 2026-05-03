class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count, s2count = {}, {}
        for x in s1:
            s1count[x] = s1count.get(x, 0) + 1
        for x in range(0, len(s1)):
            s2count[s2[x]] = s2count.get(s2[x], 0) + 1
        if s1count == s2count:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            s2count[s2[l]] -= 1
            if s2count[s2[l]] == 0:
                del s2count[s2[l]]
            s2count[s2[r]] = s2count.get(s2[r], 0) + 1
            if s1count == s2count:
                return True
            l += 1
        return False
