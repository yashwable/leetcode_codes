/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode();
        ListNode point = l3;
        int cap = 0;
        
        while(l1 != null && l2 != null){
            point.val = l1.val + l2.val + cap ;

            if (point.val > 9){
                cap = 1;
                point.val = point.val - 10 ;
            } else {
                cap = 0;
            }

            if (l1.next == null && l2.next == null && cap == 0 ){
                return l3;
            } else {
                point.next = new ListNode();
                point = point.next;
            }

            if (l1.next != null){
                l1 = l1.next;
            } else {
                l1.val = 0;
            }
            if (l2.next != null){
                l2 = l2.next;
            } else {
                l2.val = 0;
            }

        }
        return l3;
    }
}
