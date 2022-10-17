class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list1 = set(list(sentence))
        if len(list1) == 26 :
            return True
        else:
            return False
