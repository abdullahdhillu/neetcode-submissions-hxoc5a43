class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashSet = set()
        if s == "":
            return 0
        i = 0
        res = 0
        for j in range(n): 
            if s[j] not in hashSet:
                hashSet.add(s[j])
                res = max(res , j - i + 1)
            else:
                while s[j] in hashSet:
                    hashSet.remove(s[i])
                    i += 1
                hashSet.add(s[j])
        return res


        
        