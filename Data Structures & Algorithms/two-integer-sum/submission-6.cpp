class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> result;
        int target_value;
        for (int i = 0; i < nums.size(); i++){
            target_value = target - nums[i];
            if (std::find(nums.begin() + 1 + i, nums.end(), target_value)!=nums.end()){
                auto iterator = std::find(nums.begin() + 1 + i, nums.end(), target_value);
                result.push_back(i);
                result.push_back(std::distance(nums.begin(), iterator));
                return result;
            }
        }
        return result;
    }
};
