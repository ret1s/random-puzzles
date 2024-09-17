class Solution {
    public int characterReplacement(String s, int k) {
        int[] arr = new int[26];

        int res = 0, max = 0, i = 0;
        for (int j = 0; j < s.length(); j++) {
            arr[s.charAt(j) - 'A']++;
            max = Math.max(max, arr[s.charAt(j) - 'A']); // most frequent character in current window

            if (j - i + 1 - max > k) {
                arr[s.charAt(i) - 'A']--;
                i++;
                continue;
            }
            res = Math.max(res, j -i + 1);
        }

        return res;
    }
}
