class Solution {
    public int[] arrayRankTransform(int[] arr) {
        Map<Integer, Integer> rank = new HashMap<>();
        int[] sorted = Arrays.stream(arr).distinct().sorted().toArray();

        for (int i = 0; i < sorted.length; i++) {
            rank.put(sorted[i], i + 1);
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i] = rank.get(arr[i]);
        }

        return arr;
    }
}