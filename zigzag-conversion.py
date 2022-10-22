class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s 
        ans = [""] * numRows
        index , step = 0 , 1
        for i in s:
            ans[index] += i 
            if index == numRows - 1:
                step = -1
            elif index == 0 :
                step = 1
            index += step 
        return "".join(ans)
