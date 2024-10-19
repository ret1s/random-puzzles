class Solution {
    public boolean reportSpam(String[] message, String[] bannedWords) {
        Set<String> restricted = new HashSet<>(Arrays.asList(bannedWords));
        int count = 0;
        for (String m : message) {
            if (restricted.contains(m)) count++;
        }
        return count > 1;
    }
}