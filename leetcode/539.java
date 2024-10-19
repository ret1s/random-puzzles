class Solution {
    public int findMinDifference(List<String> timePoints) {
        int[] times = new int[timePoints.size()];
        int count = 0;
        for (String t : timePoints) {
            times[count++] = Integer.parseInt(t.substring(0, 2)) * 60 + Integer.parseInt(t.substring(3));
        }
        Arrays.sort(times);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < times.length - 1; i++) {
            int time = times[i + 1] - times[i];
            if (time > 12*60) time = 24*60 - time;
            res = Math.min(res, time);
        }
        return Math.min(res, 24*60 - times[times.length - 1] + times[0]);
    }
}