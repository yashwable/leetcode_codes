class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return "1"
        else :
            n = Solution().countAndSay(n-1)
            digit = n[0]
            count = 1
            ans = str(count) + digit
            for i in n[1:] :
                if i == digit :
                    count += 1
                    ans = ans[:-2]
                    ans += str(count) + digit
                else:
                    digit = i 
                    count = 1
                    ans += str(count) + digit
            return ans

