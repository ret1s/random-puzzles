class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // find the top of the mountain array in O(log(arr.length)) time complexity
        int low = 0, high = arr.size() - 1;
        int mid;
        while (high >= low) {
            mid = (low + high) / 2;
            if (mid == 0) {
                if (arr[mid] > arr[mid + 1])
                    return mid;
                else    
                    return mid + 1;
            }
            else if (mid == arr.size() - 1) {
                if (arr[mid] > arr[mid - 1])
                    return mid;
                else 
                    return mid - 1;
            }
            else if (arr[mid - 1] < arr[mid] && arr[mid + 1] < arr[mid])
                return mid;
            else if (arr[mid - 1] > arr[mid] && arr[mid] > arr[mid + 1]) 
                high = mid - 1;
            else if (arr[mid + 1] > arr[mid] && arr[mid] > arr[mid - 1]) 
                low = mid + 1;
        }
        return -1;
    }
};
