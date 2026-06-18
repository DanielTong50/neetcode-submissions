class Solution {
public:
    bool isAnagram(string s, string t) {
        //string s -> need to access all letters
        //string t -> need to acess all letters
        //could do approach where we do first condition is same size
        
        string s1 = s;
        string t1 = t;

        int i = 0;
        while (i < s.length()){
            if (!t.contains(s[i])){
                return false;
            }

            t.erase(t.find(s[i]), 1);
            i++;
        }

        i = 0;
        while (i < t.length()){
            if (!s.contains(t[i])){
                return false;
            }

            s.erase(s.find(t[i]), 1);
            i++;
        }



        return true;
    }
};
