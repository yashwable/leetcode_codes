class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        open1 = list("([{")
        close1 = list(")]}")
        print (open1)
        for i in s :
            if i in open1:
                list1.append(i)
            elif len(list1) == 0:
                return False
            else:
                if list1[-1] == open1[close1.index(i)]:
                    del list1[-1]
                else :
                    return False
        if len(list1) == 0 :
            return True
       
