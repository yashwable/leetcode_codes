# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        head1 = head 
        while (head1) :
            head1 = head1.next
            len += 1
        
        if n == len:
            return head.next
        
        len1 = 0
        head1 = head
        while len1 <  len - n -1  :
            len1 += 1
            head1 = head1.next
        head1.next = head1.next.next
        return head

        

        
        
