class Solution {
public:
    int totalMoney(int n) {
        int a = n / 7, b = n % 7; 
        int res = 0;
        res += a * 28;
        if (a > 1) 
            res += 7 * (a - 1) * a / 2;
        res += a * b + b * (b + 1) / 2;
        return res;
    }
};