class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list1 = []

        def recursion (openN,closeN ,stack ,cond):
            if openN == closeN == 0:
                list1.append(cond)
                return
            if openN > 0:
                recursion(openN - 1,closeN,stack+1,cond+"(")
            if closeN > 0 and stack > 0 :
                recursion(openN,closeN - 1,stack -1 ,cond+")")
        recursion(n,n,0,"")      
        
        return list1
