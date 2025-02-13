class Solution {
    int minOperations(int[] nums, int k) {
        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        for(int n: nums) minHeap.add((long)n);
        int count = 0;
        for(; minHeap.peek() < k; ++count) minHeap.add(minHeap.poll() * 2L + minHeap.poll());
        return count;
    }
}