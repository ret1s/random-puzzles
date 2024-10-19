// class Solution {
//     public int[] xorQueries(int[] arr, int[][] queries) {
//         int[] res = new int[queries.length];
//         for (int i = 0; i < queries.length; i++) {
//             if (queries[i][0] == queries[i][1])
//                 res[i] = arr[queries[i][0]];
//             else {
//                 int temp = arr[queries[i][0]];
//                 for (int j = queries[i][0] + 1; j <= queries[i][1]; j++) {
//                     temp ^= arr[j];
//                 }
//                 res[i] = temp;
//             }
//         }
//         return res;
//     }
// }
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] res = new int[queries.length];
        int[] prefix = new int[arr.length];
        prefix[0] = arr[0];
        for (int i = 1; i < arr.length; i++) {
            prefix[i] = prefix[i - 1] ^ arr[i];
        }

        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0], right = queries[i][1];
            if (left == 0)
                res[i] = prefix[right];
            else
                res[i] = prefix[right] ^ prefix[left - 1];
        }
        return res;
    }
}