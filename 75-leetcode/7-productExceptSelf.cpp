class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> res(size);
        vector<int> left_product(size);
        vector<int> right_product(size);
        left_product[0] = 1;
        right_product[size - 1] = 1;
        for (int i = 1; i < size; i++) {
            left_product[i] = left_product[i - 1] * nums[i - 1];
        }
        for (int i = size - 2; i >= 0; i--) {
            right_product[i] = right_product[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < size; i++) {
            res[i] = left_product[i] * right_product[i];
        }
        return res;
    }
};
// 16-08-2023
