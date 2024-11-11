class Solution {
    private static boolean[] prime;
    
    private void seive(int n){
        if(prime == null){
            // will be printed only 1 time for all test cases, so no recalculation for each test case :)
            System.out.println("Creating first seive");
            prime = new boolean[n + 1];
            Arrays.fill(prime, true);
            prime[1] = false;

            for (int p = 2; p * p <= n; p++) {
                if (prime[p] == true) {
                    for (int i = p * p; i <= n; i += p)
                        prime[i] = false;
                }
            }
        }else{
            // do nothing
            // System.out.println("Doing nothing, seive already calculated");
        }
    }
    public boolean primeSubOperation(int[] nums) {
        seive(1000);
        
        int j = 0, smallestTillNow = 1;
        
        while(j < nums.length){
            
            // We need to make the left elements as small as possible so that right can be made
            int diff = nums[j] - smallestTillNow;
            if(diff < 0){
                // Now nothing can help us, array can't be made increasing, so return false
                return false;
            }
            // System.out.println(diff + " - " + j);
            // means we need to substrace the diff from nums[j], but we can only do this if nums[j] is prime
            if(prime[diff] || diff == 0){
                // for strictly increasing, we are incrementing this as well
                // to ensure the next checked would surely be stricly increasing.
                // if we don't increase smallestTillNow, then it would give increasing result
                // instead of strictly increasing
                smallestTillNow++;
                j++;
            }else{
                smallestTillNow++;
            }
        }
        return true;
    }
}