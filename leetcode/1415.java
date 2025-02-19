class Solution {
    public String getHappyString(int n, int k) {
        int prem = 1 << (n - 1);
        if (k > 3 * prem)
            return "";
        int ch = 'a' + (k - 1) / prem;
        StringBuilder sb = new StringBuilder(Character.toString(ch));
        while (prem > 1) {
            k = (k - 1) % prem + 1;
            prem >>= 1;
            ch = (k - 1) / prem == 0 ? 'a' + (ch == 'a' ? 1 : 0) : 'b' + (ch != 'c' ? 1 : 0);
            sb.append((char)ch);
        }
        return sb.toString();
    }  
}