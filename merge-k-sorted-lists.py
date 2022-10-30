# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p1 = ListNode()
        pointer = p1
        while True:
            pointer1 = None
            max1 = None
            for i in range(len(lists)):
                if lists[i].val and lists[i] > max1:
                    max1 = lists[i].val
                    pointer1 = lists[i]
