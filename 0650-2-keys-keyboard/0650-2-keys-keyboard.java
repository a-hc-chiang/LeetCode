class Solution {
    public int minSteps(int n) { //dynamic programming solution 
        if (n == 1) //base case 1
            return 0; 
        if (isPrime(n)) //base case 2
            return n; 
        
        int minVal = Integer.MAX_VALUE; //to shrink over time 
        for (int i = 2; i < n/2; i++) { //finding factors to break n down 
            if (n % i == 0) { 
                minVal = Math.min(minVal, i+minSteps(n/i)); 
            }
        }
        return minVal; 
    }

    private boolean isPrime(int n) { //helper method to find if n is prime
        for (int i = 2; i < n/2; i++)
            if (n % i == 0)
                return false;
        return true;
    }
}