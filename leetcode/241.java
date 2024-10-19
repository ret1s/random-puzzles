class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> res = new LinkedList<Integer>();
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '-' || expression.charAt(i) == '+' || expression.charAt(i) == '*') {
                String op1 = expression.substring(0, i);
                String op2 = expression.substring(i + 1);
                List<Integer> op1Res = diffWaysToCompute(op1);
                List<Integer> op2Res = diffWaysToCompute(op2);
                for (int p1 : op1Res) {
                    for (int p2 : op2Res) {
                        int c = 0;
                        switch (expression.charAt(i)) {
                            case '+': c = p1 + p2;
                                break;
                            case '-': c = p1 - p2;
                                break;
                            case '*': c = p1 * p2;
                                break;
                        }
                        res.add(c);
                    }
                }
            }
        }
        if (res.size() == 0) {
            res.add(Integer.valueOf(expression));
        }
        return res;
    }
}