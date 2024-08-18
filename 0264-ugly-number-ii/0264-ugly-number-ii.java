class Solution {
    public int nthUglyNumber(int n) {
        if (n == 1) 
            return 1; 

        TreeSet<Long> set = new TreeSet<>(); 
        set.add(1L); // Start with 1 as the first ugly number
        
        int count = 1;
        long uglyNumber = 1;
        
        while (count < n) {
            uglyNumber = set.pollFirst(); // Get and remove the smallest element
            set.add(uglyNumber * 2);
            set.add(uglyNumber * 3);
            set.add(uglyNumber * 5);
            count++;
        }
        return Math.toIntExact(set.pollFirst());
    }
}