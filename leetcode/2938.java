class Solution {
    public long minimumSteps(String s) {
        long res = 0;
        long count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                res += i - count;
                count++;
            }
        }
        return res;
    }
}