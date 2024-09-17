class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0, l = 0;
        HashSet<Character> charSet = new HashSet<>();

        for (int r = 0; r < s.length(); r++) {
            while(charSet.contains(s.charAt(r))) {
                charSet.remove(s.charAt(l));
                l++;
            }
            charSet.add(s.charAt(r));
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
