class Solution {
    public int getLucky(String s, int k) {
        int sum = 0;
        for (char ch : s.toCharArray()) sum += sumDigit(ch - 'a' + 1);
        while (k - 1 > 0) {
            sum = sumDigit(sum);
            k--;
        }
        return sum;
    }
    public int sumDigit(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num%10;
            num /= 10;
        }
        return sum;
    }
}   