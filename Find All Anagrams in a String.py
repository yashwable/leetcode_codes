class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        arr1 = [0]*26
        for i in p:
            arr1[ord(i)-97] += 1
        
        ans = []
        
        arr2 = [0]*26
        r = 0
        f = r + len(p)

        for i in range(r,f):
            arr2[ord(s[i]) - 97] += 1 

        if arr2 == arr1:
            ans.append(r)

        for i in range(1,len(s)-len(p)+1):
            arr2[ord(s[r]) - 97] -= 1
            r += 1
            arr2[ord(s[f]) - 97] += 1
            f += 1
            if arr2 == arr1:
                ans.append(r) 
        
        return ans
