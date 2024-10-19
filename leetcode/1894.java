public class 1894 {
    class Solution {
        public int chalkReplacer(int[] chalk, int k) {
            long total = 0;
            for (int c : chalk) total += c;
            k %= total;
            for (int i = 0; i < chalk.length; i++) {
                if (chalk[i] > k) return i;
                k -= chalk[i];
            }
            return -1;
        }
    }
}
