class Solution {
public:
    bool isValid(string s) {
        while (s.size() > 0) {
            std::cout << s << std::endl;
            if (s.find("()") != -1) {
                s.erase(s.begin() + s.find("()"), s.begin() + s.find("()") + 2);
            } else if (s.find("{}") != -1) {
                s.erase(s.begin() + s.find("{}"), s.begin() + s.find("{}") + 2);
            } else if (s.find("[]") != -1) {
                s.erase(s.begin() + s.find("[]"), s.begin() + s.find("[]") + 2);
            } else {
                return false;
            }
        }
        return true;
    }
};


// (([])){}
