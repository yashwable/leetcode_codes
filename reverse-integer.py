class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        
        num = 214748364
        ans = 0
        
        while x != 0 :
            n = x % 10
            if ans < num:
                ans = 10*ans + n
            elif ans == num :
                if x < 0:
                    if n <= 8:
                        ans = 10*ans + n 
                    else :
                        return 0
                else:
                    if n <= 7:
                        ans = 10*ans + n 
                    else :
                        return 0
            else:
                return 0
            x = x // 10
            print (n)
        if neg:
            return ans * -1
        return ans
        

