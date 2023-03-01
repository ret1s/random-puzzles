class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        int mid, res;
        while (high >= low) {
            mid = (high + low) / 2;
            if (nums[mid] == target)
                return mid;
            else if (target > nums[mid]) 
                low = mid + 1;
            else if (target < nums[mid])
                high = mid - 1;
        } 
        if (target > nums[mid]) 
            res = mid + 1;
        else 
            res = mid;
        return res;
    }
};
