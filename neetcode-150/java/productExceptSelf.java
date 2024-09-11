// BRUTEFORCE SOLUTION:
// class Solution {
//     public int[] productExceptSelf(int[] nums) {
//         int[] res = new int[nums.length];
//         Arrays.fill(res, 1);
//         for (int i = 0; i < nums.length; i++) {
//             for (int j = 0; j < nums.length; j++) {
//                 if (i != j) {
//                     res[j] *= nums[i];
//                 }
//             }
//         }
//         return res;
//     }
// }  
// ====================
// OPTIMAL SOLUTION
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int right = 1, left = 1;
        for (int i = 0; i < nums.length; i++) {
            res[i] = left;
            left *= nums[i];
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
}  
