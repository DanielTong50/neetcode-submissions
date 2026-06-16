class Solution {
public:
    int calPoints(vector<string>& operations) {
        std::vector<int> results;
        int result = 0;
        int i = 0;
        while (i < operations.size()){
            if (operations[i] == "C"){
                results.pop_back();
            }
            else if (operations[i] == "D"){
                results.push_back(results.back()*2);
            }

            else if (operations[i] == "+"){
                results.push_back(results[results.size()-1]+results[results.size()-2]);
            }
            else{
                results.push_back(std::stoi(operations[i]));
            }
            i++;
        }

        for (int j = 0; j < results.size(); j++){
            result+=results[j];
        }

        return result;
    }
};