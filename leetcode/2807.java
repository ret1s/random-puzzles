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
    static int findGCD(int a, int b) {
        if (b == 0) return a;
        return findGCD(b, a % b);
    }

    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode cur = head;
        ListNode nxt = cur.next;
        while (cur != null && nxt != null) {
            int r = findGCD(cur.val, nxt.val);
            ListNode g = new ListNode(r);
            cur.next = g;
            g.next = nxt;
            cur = nxt;
            nxt = cur.next;
        }
        return head;
    }
}