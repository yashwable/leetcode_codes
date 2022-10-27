# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        l11 = l1
        l21 = l2
        p1 = ListNode()
        first_time = True
        cap = 0
        while l11.next != None or l21.next != None:
            while l11.next :
                l11 = l11.next
            while l21.next :
                l21 = l21.next

            p2 = ListNode(l11.val + l21.val + cap)
            if p2.val > 9:
                p2.val = p2.val - 10
                cap = 1
            else :
                cap = 0
            if p1.val == 0 and first_time:
                p1 = p2
                first_time = False
            else:
                last = p1
                while last.next :
                    last = last.next 
                last.next = p2
            l12 = l1
            l22 = l2
            while l12.next and l12.next.next:
                l12 = l12.next
            l12.next = None
            while l22.next and l22.next.next:
                l22 = l22.next
            l22.next = None
            l11 = l1
            l21 = l2
        return p1
