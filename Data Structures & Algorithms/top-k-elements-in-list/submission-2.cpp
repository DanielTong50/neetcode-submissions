class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> result;
        vector<int> seen;
        unordered_map<int, int> freq;
        for (int x : nums) {
            freq[x]++;
        }

        sort(nums.begin(), nums.end(), [&](int a, int b) {
            return freq[a] > freq[b];
        });

        int i = 0;
        while (i < nums.size() && k > 0){
            if (!std::ranges::contains(seen, nums[i])){
                seen.push_back(nums[i]);
                result.push_back(nums[i]);
                k--;
            }
            i++;
        }
        return result;
    }
};
