import java.util.*;

class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int total = 0;
        for (int r : rolls) {
            total += r;
        }
        int s = mean * (n + rolls.length) - total;
        int[] res = new int[n];
        if (s < n || s > n * 6)
            return new int[0];
        int a = s / n, r = s % n ;
        Arrays.fill(res, a);
        for (int i = 0; i < r; i ++) {
            res[i]++;
        }
        return res;
    }
}
