class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j <= s.size() - i; j++) {
                string temp = s.substr(j, i);
                string re_temp = temp;
                reverse(re_temp.begin(), re_temp.end());
                if (temp == re_temp) {
                    count++;
                }
            }
        }
        return count;
    }
};