class Solution {
    public double findMaxAverage(int[] nums, int k) {
        if (nums.length == 1)
            return (double) nums[0];
        
        int start = 0, end = k;
        double avg = 0;

        for (int i = 0; i < k; i++) {
            avg += (double) nums[i] / k;
        }

        double max = avg;

        while (end < nums.length) {
            avg -= (double) nums[start++] / k;
            avg += (double) nums[end++] / k;

            max = Math.max(avg, max);
        }

        return max;
    }
}
