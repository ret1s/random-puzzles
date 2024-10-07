class Solution {
    public int minLength(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (stack.isEmpty()) {
                stack.push(cur);
                continue;
            }
            if (cur == 'B' && stack.peek() == 'A') {
                stack.pop();
            }
            else if (cur == 'D' && stack.peek() == 'C') {
                stack.pop();
            } 
            else {
                stack.push(cur);
            }
        }

        return stack.size();
    }
}