class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        //relative order arr2
        vector<int> result1;
        vector<int> result2;
        
        //look through all of arr1 to see first element of arr2
        for (int i = 0; i < arr2.size(); i++){
            for (int j = 0; j < arr1.size(); j++){
                if (arr1[j] == arr2[i]){
                    result1.push_back(arr1[j]);
                }
            }
        }

        for (int i = 0; i < arr1.size(); i++){
            bool valid = true;

            for (int j = 0; j < arr2.size(); j++){
                if (arr1[i] == arr2[j]){
                    valid = false;
                    break;
                }
            }
            if (valid){
                result2.push_back(arr1[i]);
            }

        }


        for (int i = 0; i < result2.size()-1; i++){
            int largest = result2[i];
            int index = i;
            for (int j = i +1; j < result2.size(); j++){
                if (result2[j] >= largest){
                    largest = result2[j];
                    index = j;
                }
            }
            result2[index] = result2[i];
            result2[i] = largest;
        }

        int final_size = result2.size();

        for (int i = 0; i < final_size; i++){
            result1.push_back(result2.back());
            result2.pop_back();
        }

        return result1;
    }
};