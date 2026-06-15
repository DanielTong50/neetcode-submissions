class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       std::unordered_set<int> seen;
        int i = 0;
        int n = nums.size();

        while (i < n) {
            // Check if current element is in the set
            if (seen.find(nums[i]) != seen.end()) {
                return true;
            }
            seen.insert(nums[i]);
            i++; // Increment the index manually
        }
        
        return false;
    }
};