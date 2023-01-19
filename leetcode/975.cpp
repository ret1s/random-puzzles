class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int res = 0, prefixRem = 0;
        int n = nums.size();
        vector<int> remList(k);
        remList[0] = 1;   
        for (int i = 0; i < n; i++) {
            prefixRem = (prefixRem + nums[i] % k + k) % k;
            res += remList[prefixRem];
            remList[prefixRem]++;
        }
        return res;
    }
};
