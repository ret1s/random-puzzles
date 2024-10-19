class Solution {
    public int findComplement(int num) {
        int base = 1;
        int a = 0;
        int tmp = num;
        int res = 0;
        while (tmp != 0) {
            res += (tmp % 2 == 0) ?  Math.pow(2, a) : 0;
            tmp /= 2;
            base *= 10;
            a++;
        }
        return res;
    }
}