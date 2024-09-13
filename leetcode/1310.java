class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            if (queries[i][0] == queries[i][1])
                res[i] = arr[queries[i][0]];
            else {
                int temp = arr[queries[i][0]];
                for (int j = queries[i][0] + 1; j <= queries[i][1]; j++) {
                    temp ^= arr[j];
                }
                res[i] = temp;
            }
        }
        return res;
    }
}