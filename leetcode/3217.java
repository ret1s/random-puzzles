import java.util.*;

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
    public ListNode modifiedList(int[] nums, ListNode head) {
        ListNode res = new ListNode(-1);
        ListNode tmp = res;
        Set<Integer> s = new HashSet<>();
        for (int num : nums) s.add(num);

        while (head != null) {
            if (!s.contains(head.val)) {
                tmp.next = head;
                tmp = tmp.next;
            }
            head = head.next;
        }

        tmp.next = null;
        return res.next;
    }
}