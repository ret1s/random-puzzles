class Solution {
public:
    int helper(int n) {
        int res = 0;
        while (n > 0) {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }

    bool isHappy(int n) {
        set<int> setofSum;
        while (n > 1 && setofSum.count(n) == 0) {
            setofSum.insert(n);
            n = helper(n);
        }
        return n == 1;
    }
};
