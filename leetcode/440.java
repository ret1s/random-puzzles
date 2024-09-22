class Solution {
    public int findKthNumber(int n, int k) {
        int cur = 1;
        k--;
        while (k > 0) {
            int step = cal(n, cur, cur + 1);
            if (step <= k) {
                cur++;
                k -= step;
            } else {
                cur *= 10;
                k--;
            }
        }
        return cur;
    }

    public int cal(int n, long n1, long n2) {
        int step = 0;
        while (n1 <= n) {
            step += Math.min(n + 1, n2) - n1;
            n1 *= 10;
            n2 *= 10;
        }
        return step;
    }
}