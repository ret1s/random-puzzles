class Solution {
public:
    int maxArea(vector<int>& height) {
        int size = height.size();
        int start = 0, end = size - 1;
        int max = -1;
        while (start <= end) {
            int h = (height[start] <= height[end]) ? height[start] : height[end];
            int area = h * (end - start);
            if (area > max)
                max = area;
            if (height[start] < height[end])
                start++;
            else 
                end--;
        }
        return max;
    }
};
