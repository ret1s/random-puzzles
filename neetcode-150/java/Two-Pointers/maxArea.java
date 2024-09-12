class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1, res = 0;
        while (left < right) {
            int length = right - left;
            int area = length * Math.min(heights[left], heights[right]);
            res = Math.max(res, area);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return res;
    }
}
