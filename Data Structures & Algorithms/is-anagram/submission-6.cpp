class Solution {
public:
    bool isAnagram(string s, string t) {
        
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
