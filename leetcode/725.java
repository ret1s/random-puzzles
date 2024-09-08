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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode tmp = head;
        int count = 0;
        while (tmp != null) {
            count++;
            tmp = tmp.next;
        }

        tmp = head;
        ListNode[] res = new ListNode[k];
        if (count < k) {
            for (int i = 0; i < count; i++) {
                res[i] = tmp;
                ListNode a = tmp.next;
                tmp.next = null;
                tmp = a;
            }    
        } else {
            int m = count/k, n = count%k;
            for (int i = 0; i < k; i++) {
                res[i] = tmp;
                int size = m;
                if (n > 0) {
                    size++;
                    n--;
                }
                for (int j = 0; j < size - 1; j++) {
                    tmp = tmp.next;
                }
                ListNode a = tmp.next;
                tmp.next = null;
                tmp = a;
            }
        }

        return res;
    }
}