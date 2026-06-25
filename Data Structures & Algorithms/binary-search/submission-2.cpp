class Solution {
public:
    int search(vector<int>& nums, int target) {
        return search_target(nums, target, 0, nums.size() -1);
    }

    int search_target(vector<int>& nums, int target, int num_start, int num_stop){
        int mid = num_start + (num_stop - num_start)/2;

        if (num_stop < num_start){
            return -1;
        }

        if (nums[mid] == target){
            return mid;
        }
        if (nums[mid] > target){
            return search_target(nums, target, num_start, mid -1);
        }
        if (nums[mid] < target){
            return search_target(nums, target, mid + 1, num_stop);
        }

        return -1;
    }
};
