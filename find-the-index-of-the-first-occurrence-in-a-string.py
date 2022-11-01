class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(needle)
        if len(haystack) < len1:
            return -1
        for i in range(len(haystack)):
            if haystack[i:i + len1] == needle:
                return i 
        else :
            return -1
            
