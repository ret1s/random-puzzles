class Solution {
    public String largestNumber(int[] nums) {
        String[] a = new String[nums.length];
        int count = 0;
        for (int num : nums) {
            a[count++] = Integer.toString(num);
        }
        Arrays.sort(a, (m, n)->(n + m).compareTo(m + n));
        if (a[0].equals("0")) return "0";
        StringBuilder res = new StringBuilder();
        for(String s : a) res.append(s);
        return res.toString();
    }
}