class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] a1 = s1.split(" ");
        String[] a2 = s2.split(" ");
        Map<String, Integer> m = new HashMap<>();
        for (String word : a1) {
            m.put(word, m.getOrDefault(word, 0) + 1);
        }
        for (String word : a2) {
            m.put(word, m.getOrDefault(word, 0) + 1);
        }
        List<String> w = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : m.entrySet()) {
            if (entry.getValue() == 1) w.add(entry.getKey());
        }
        return w.toArray(new String[0]);
    }
}