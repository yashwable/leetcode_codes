class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr1 = []
        list1 = []
        def rec (i,candidates0,arr,target,list0):
            if i == len(candidates0):
                if target == 0:
                    arr.append(list0)
                return 
            if candidates0[i] <= target :
                list0.append(candidates0[i])
                rec(i,candidates0,arr,target - candidates0[i],list0)
                list0.remove(list0[-1])
            rec(i+1,candidates0,arr,target,list0)
        rec(0,candidates,arr1,target,list1)
        return arr1
