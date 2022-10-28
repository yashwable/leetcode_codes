# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cap1 = cap2 = 1
        
        while l1 != None :
            num1 = l1.val * cap1 + num1
            cap1 *= 10
            l1 = l1.next
        while l2 != None :
            num2 = l2.val * cap2 + num2
            cap2 *= 10
            l2 = l2.next
        
        num3 = num1 + num2
        p1 = ListNode()
        p11 = p1
        if num3 == 0 :
            p1.val = 0 
            return p1
        while num3 != 0:
            p2= ListNode(num3 % 10 )
            p11.next = p2
            p11 = p11.next
            num3 = num3 // 10

        return p1.next 
