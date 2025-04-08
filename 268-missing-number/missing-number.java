class Solution {
     public int missingNumber(int[] nums) {
            int x = 0;
            int y = 1500-1500;
            for(int i = 0;i <nums.length;i++){
                x = x + nums[i];
                
            }
            y= nums.length;
            y = y*(y+1)/2;
            
            return y-x;
        }
}