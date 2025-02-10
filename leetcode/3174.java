class Solution {
    public String clearDigits(String s) {
        int n = s.length();
        StringBuilder sb = new StringBuilder(s);

        int i = 0;
        while (i < n) {
            // Check if the current character is a digit
            if (sb.charAt(i) >= '0' && sb.charAt(i) <= '9') {
                sb.setCharAt(i, '!'); // Mark the digit for deletion
                // Find the closest non-digit character to the left
                for (int j = i - 1; j >= 0; j--) {
                    if ((sb.charAt(j) < '0' || sb.charAt(j) > '9') && sb.charAt(j) != '!') {
                        sb.setCharAt(j, '!'); // Mark the non-digit character for deletion
                        break;
                    }
                }
            }
            i++;
        }
        // Build the resulting string without the marked characters
        StringBuilder res = new StringBuilder();
        for (int k = 0; k < n; k++) {
            if (sb.charAt(k) != '!') res.append(sb.charAt(k));
        }
        return res.toString();
    }
}