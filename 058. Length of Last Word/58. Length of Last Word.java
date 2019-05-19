/**
方法来源：https://blog.csdn.net/mikuluna/article/details/84347221
直接先去两边空格，然后倒叙，如果不是空格，则count++；
如果是空格，就直接退出循环。最后这个count就是单词长度

*/
class Solution {
    public int lengthOfLastWord(String s) {
        int len = s.length();
        s = s.trim();
        int count = 0;
        for(int i = s.length() - 1;i >= 0; i--){
            if(s.charAt(i) != ' '){
                count++;
            }else {
                break;
            }
        }
        return count;
    }
}