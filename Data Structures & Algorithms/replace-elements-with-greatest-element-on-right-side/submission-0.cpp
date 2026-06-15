class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        for (int i = 0; i < arr.size()-1; i++){
            int j = i+1;
            int max = arr[i+1];
            while (j < arr.size()){
                if (arr[j] > max){
                    max = arr[j];
                }
                j++;
            }

            arr[i] = max;
        }
        arr[arr.size()-1] = -1;
        return arr;
    }
};