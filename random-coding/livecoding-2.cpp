#include <bits/stdc++.h>
using namespace std;

int reverse(int x) {
    int res = 0;
    // reverse
    while (x != 0) {
        res = res*10 + x%10;
        x /= 10;
        if ((INT_MAX - res)/10 < (x%10) * 100000000 || INT_MIN - res < (x%10) * -1000000000)
            return 0;
    }
    return res;
}

int main() {
    // vector<int> nums = {3, 3};
    // int target = 6;
    // vector<int> array(1000, -1);
    // for (int i = 0; i < nums.size(); i++) {
    //     if (array[target - nums[i]] != -1) {
    //         cout << i << " " << array[target - nums[i]];
    //         break;
    //     }
    //     array[nums[i]] = i;
    // }
    cout << reverse(3147483648) << endl;
    cout << (int) 3147483648 << endl;
    return 0;
}

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Input: nums = [2,7,11,15], target = 9 
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].