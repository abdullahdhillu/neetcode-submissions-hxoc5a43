class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1, set2 = {}, {}
        for ch in s:
            set1[ch] = set1.get(ch, 0) + 1
        for ch in t:
            set2[ch] = set2.get(ch, 0) + 1
        return set1 == set2