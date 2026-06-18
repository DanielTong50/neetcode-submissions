class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> answer;
        int i = 0;
        while (i < nums.size()-1){
            int j = i + 1;
            while (j < nums.size()){
                if (nums[i] + nums[j] == target){
                    answer.push_back(i);
                    answer.push_back(j);
                    return answer;
                }
                j++;
            }
            i++;
        }

        return answer;
    }
};
