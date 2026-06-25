class KthLargest {
public:
    
    int capacity;
    std::vector<int> arr_k;
    std::vector<int> temp;

    KthLargest(int k, vector<int>& nums) {
        capacity = k;
        temp = nums;
        std::sort(temp.begin(), temp.end(), std::greater<int>());
        for (int i = 0; i < k && i < temp.size(); i++){
            arr_k.push_back(temp[i]);
        }
    }   
    
    int add(int val) {
        arr_k.push_back(val);
        std::sort(arr_k.begin(), arr_k.end(), std::greater<int>());
        if (arr_k.size()  > capacity){
            arr_k.pop_back();
        }
        
        return arr_k[arr_k.size()-1];
    }
};
