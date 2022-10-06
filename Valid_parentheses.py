class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        for i in s :
            if i in "([{":
                list1.append(i)
            elif (len(list1) != 0 ):
                if i == ")" and "(" == list1[-1] :
                    del list1[-1]
                elif i == "]" and "[" == list1[-1] :
                    del list1[-1]
                elif i == "}" and "{" == list1[-1] :
                    del list1[-1]
                else: 
                    return False
            else:
                return False
        if len(list1) == 0:
            return True
