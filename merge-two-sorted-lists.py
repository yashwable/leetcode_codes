# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = ListNode()
        pointer = p1
        while True:
            if list1 or list2 :
                pointer.next = ListNode()
                pointer = pointer.next
            else:
                return p1.next

            if list1 == None:
                pointer.val = list2.val
                list2 = list2.next

            elif list2 == None:
                pointer.val = list1.val
                list1 = list1.next
                
            elif list1.val <= list2.val :
                pointer.val = list1.val
                list1 = list1.next
                
            else :
                pointer.val = list2.val
                list2 = list2.next
               
                
