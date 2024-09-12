class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        Map<Character, Character> bracketLookup = new HashMap<>(3);
        bracketLookup.put(')', '(');
        bracketLookup.put('}', '{');
        bracketLookup.put(']', '[');
        for (char c : s.toCharArray()) {
            if (bracketLookup.containsKey(c)) {
                if (brackets.empty() || !bracketLookup.get(c).equals(brackets.peek()))
                    return false;
                else
                    brackets.pop();
            } else {
                brackets.push(c);
            }
        }
        return brackets.empty();
    }
}
