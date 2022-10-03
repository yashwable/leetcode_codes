class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = min(strs,key = len)
        for i in minstr:
            for j in strs:
                return i
