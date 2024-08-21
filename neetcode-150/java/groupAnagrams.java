class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String key = Arrays.toString(count); // anagram key of current string 
            if (!res.containsKey(key)) {
                res.put(key, new ArrayList<>()); // create if anagram key doesn't exist
            }
            res.get(key).add(s); // put value of current string
        }
        return new ArrayList<>(res.values());
    }
}
