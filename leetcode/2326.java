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
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] res = new int[m][];
        for (int i = 0; i < m; i++) {
            res[i] = new int[n];
            Arrays.fill(res[i], -1);
        }

        int TR = 0, BR = m - 1, LC = 0, RC = n - 1;
        while (head != null) {
            for (int i = LC; i <= RC && head != null; i++) {
                res[TR][i] = head.val;
                head = head.next;
            }
            TR++;

            for (int i = TR; i <= BR && head != null; i++) {
                res[i][RC] = head.val;
                head = head.next;
            }
            RC--;

            for (int i = RC; i >= LC && head != null; i--) {
                res[BR][i] = head.val;
                head = head.next;
            }
            BR--;

            for (int i = BR; i >= TR && head != null; i--) {
                res[i][LC] = head.val;
                head = head.next;
            }
            LC++;
        }

        return res;
    }
}