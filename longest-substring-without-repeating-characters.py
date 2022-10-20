class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list1 = []
        count0 = 0
        for i in range(len(s)):
            if s[i] not in list1:
                list1.append (s[i])
            else:
                list1 = list1[list1.index(s[i])+1:]
                list1.append(s[i])
            if len(list1) > count0:
                count0 = len(list1)
            
        return count0
