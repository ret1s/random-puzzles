# LEETCODE 150 NOTES
### 15/11/2023
Today, I practiced problems that use two pointers technique approach.
Here are some notes:
* In twoSum problem, using hash map data structure is a good approach if the array is unsorted. When the given array is sorted, using two pointers will be a better approach. 
* threeSum problem is an extended version of twoSum problems. To solve it, we can use past results achieved from twoSum problems. In detail, we first sort the given array into one that has non-decreasing order. Then we traverse the array from start to end, use the current traverse element as the target in twoSum and the rest array as the input array in twoSum. Remember that because the elements in the given array can be exactly the same, we have to use set data structure to store the found results. And to reduce the time complexity of the algorithm, we can break the big loop when the current traverse element is larger than zero. 
* maxArea is just an extended version of twoSum.
* isPalindrome and isSubsequence are quite straightforward. If the input array of isPalindrome contains only lowercase letters, using Stack can be a good approach.

### 16/11/2023
Today, I practiced problems about hash map.
Here are some notes:
