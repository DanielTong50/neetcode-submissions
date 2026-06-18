class Solution {
public:
    bool isAnagram(string s, string t) {
        //string s -> need to access all letters
        //string t -> need to acess all letters
        //could do approach where we do first condition is same size
        
        if (s.length()!=t.length()){
            return false;
        }

        int i = 0;
        while (i < s.length()){
            if (!t.contains(s[i])){
                return false;
            }

            t.erase(t.find(s[i]), 1);
            i++;
        }

        return true;
    }
};
