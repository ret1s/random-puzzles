class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        while (start < end) {
            int total = numbers[start] + numbers[end];
            if (total > target) {
                end--;
            }
            else if (total < target) {
                start++;
            }
            else {
                break;
            }
        }
        return new int[] {start + 1, end + 1};
    }
}
