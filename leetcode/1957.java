class Solution {
    public String makeFancyString(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 1;
        char prev = s.charAt(0);
        sb.append(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == prev) {
                if (count < 2) {
                    sb.append(s.charAt(i));
                }
                count++;
            } else {
                sb.append(s.charAt(i));
                count = 1;
                prev = s.charAt(i);
            }
        }
        return sb.toString();
    }
}