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
        p11 = p1
        first_time = True
        cap = 0
        while True:
            while l11.next and l11.next.next :
                l11 = l11.next
            while l21.next and l21.next.next :
                l21 = l21.next
            while p11.next:
                p11 = p11.next

            if l11.next == None and l21.next == None :
                p2= ListNode(l11.val + l21.val + cap)
                if p2.val > 9:
                    p2.val = p2.val - 10 
                    cap = 1
                else :
                    cap = 0
                p11.next = p2
                return p1.next

            elif l11.next == None :
                p2= ListNode(l11.val + l21.next.val + cap)
                if p2.val > 9:
                    p2.val = p2.val - 10 
                    cap = 1
                else :
                    cap = 0
                p11.next = p2
                l11.val = 0
                l21.next = None

            elif l21.next == None :
                p2 = ListNode(l11.next.val + l21.val + cap)
                if p2.val > 9:
                    p2.val = p2.val - 10 
                    cap = 1
                else :
                    cap = 0
                p11.next = p2
                l21.val = 0
                l11.next = None

            else:
                p2 = ListNode(l11.next.val + l21.next.val + cap)
                if p2.val > 9:
                    p2.val = p2.val - 10 
                    cap = 1
                else :
                    cap = 0
                p11.next = p2
                l11.next = None
                l21.next = None
            l11 = l1
            l21 = l2 
            
        return p1.next

            
            


                
            
