class Solution {
public:
    bool isValid(string s) {
        // If length is odd, it can't be balanced
        if (s.length() % 2 != 0) {
            return false;
        }

        std::stack<char> st;

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];

            // If it's an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // If it's a closing bracket
            else {
                // If stack is empty, there's no opener for this closer
                if (st.empty()) return false;

                char top = st.top();
                // Check if the top of the stack matches the current closer
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false; // Mismatched types
                }
            }
        }

        // If the stack is empty, all were matched correctly
        return st.empty();
 }
};