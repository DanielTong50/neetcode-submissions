class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length()-1;
        std::vector<char> alphabet = {'a', 'b', 'c','d',
        'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m',
        'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w','x','y','z', '0', '1', '2', '3', '4', '5',
        '6','7','8','9'};
        while (i < j){
            //if not member of a->z, do pointer correction
            while (i < j && (std::find(alphabet.begin(), alphabet.end(), std::tolower(s[i])) == alphabet.end())){
                i++;
            }
            while (i < j && (std::find(alphabet.begin(), alphabet.end(), std::tolower(s[j]))  == alphabet.end())){
                j--;
            }
            //check equivlance with lower case
            if (std::tolower(s[i]) != std::tolower(s[j])){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};

