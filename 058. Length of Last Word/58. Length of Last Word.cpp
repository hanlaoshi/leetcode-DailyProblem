//下面这种方法是第一种解法的优化版本，
//由于我们只关心最后一个单词的长度，
//所以开头有多少个空格其实我们并不在意，可以从字符串末尾开始，
//先将末尾的空格都去掉，然后开始找非空格的字符的长度即可。
class Solution {
public:
    int lengthOfLastWord(string s) {
        int right = s.size() - 1, res = 0;
        while (right >= 0 && s[right] == ' ') --right;
        while (right >= 0 && s[right] != ' ' ) {
            --right; 
            ++res;
        }
        return res;
    }
};