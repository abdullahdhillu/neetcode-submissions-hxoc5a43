class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)
        answer = ""
        for cnt in range(len(shortest_str)):
            for str in strs:
                if str[cnt] != shortest_str[cnt]:
                    return shortest_str[:cnt]
        return shortest_str
            

            



        