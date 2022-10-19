class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1 = {}
        list1 = []
        for i in words:
            if i not in dict1:
                dict1[i] = 1
            else :
                dict1[i] += 1
        list2 = sorted(dict1.values(),reverse = True)
        for i in range(k):
            for j in range(len(dict1)):
                if dict1[j] == list2[i]:
                    list1.append()
