class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int i = 0;
        int max = 0;
        int current = 0;
        while (i < nums.size()){
            if (nums[i] == 1){
                current++;
            } else {
                current = 0;
            }

            if (current > max){
                max = current;
            }
            i++;
        }
        return max;
    }
};