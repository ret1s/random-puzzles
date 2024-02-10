# LEETCODE 150 NOTES
### 15/11/2023
Today, I practiced problems that use two pointers technique approach.
Here are some notes:
- In twoSum problem, using hash map data structure is a good approach if the array is unsorted. When the given array is sorted, using two pointers will be a better approach. 
- threeSum problem is an extended version of twoSum problems. To solve it, we can use past results achieved from twoSum problems. In detail, we first sort the given array into one that has non-decreasing order. Then we traverse the array from start to end, use the current traverse element as the target in twoSum and the rest array as the input array in twoSum. Remember that because the elements in the given array can be exactly the same, we have to use set data structure to store the found results. And to reduce the time complexity of the algorithm, we can break the big loop when the current traverse element is larger than zero. 
- maxArea is just an extended version of twoSum.
- isPalindrome and isSubsequence are quite straightforward. If the input array of isPalindrome contains only lowercase letters, using Stack can be a good approach.
---
### 16/11/2023
Today, I practiced problems about hash map.
Here are some notes:
- In twoSum problem, using hash map data structure is a good approach if the array is unsorted. When the given array is sorted, using two pointers will be a better approach. 
- In canConstruct, we learn two basic functions can be used in hash map data structure: _find_ and _count_. To wrap up:
  + _find_: searches the container for and element with k as key and return an _iterator_ to it if found, otherwise it returns an iterator to unordered_map::end (the element past the end of the container).
  + _count_: searches the container for elements whose key is k and returns the number of elements found. Because unordered_map containers do not allow for duplicate keys, this means that the function actually returns 1 if an element with that key exists in the container, and zero otherwise.
- In isIsomorphic, we have to craft two hash maps for pairs of character in two strings so that we can keep the strong connection between two characters (both character are key).  
---
### 10/02/2023
1. Remove Element
2. Remove Duplicates