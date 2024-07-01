class Solution {
    public int removeDuplicates(int[] nums) {
        int k = nums.length;
        ArrayList<Integer> A = new ArrayList<>();
        A.add(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == A.get(A.size() - 1)) {
                k--;
            } else {
                A.add(nums[i]);
            }
        }
        for (int i = 0; i < k; i++) {
            nums[i] = A.get(i);
        }
        return k;
    }
}

/* 
class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}
EXPLAIN: 
we compare the current value with its previous value, if they are different, we found a new unique value, then we insert it to a counter variable so that we can override the original array list with a new uniqued array list.
*/