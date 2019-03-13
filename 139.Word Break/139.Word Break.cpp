class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int len=s.size();
        vector<bool> isWordBreak(len+1,false);//定义一个含有len+1个元素的vector，用于存储子问题信息
        isWordBreak[0]=true;//将第一个元素设置为true，表示当字符串为空的时候也成立
        set<string> dict;
        
        for(const auto &ss:wordDict) dict.insert(ss);
        
        for(int i=0;i<len+1;++i)
        {
            for(int j=0;j<i;++j)
            {
                if(!isWordBreak[j])//本条语句用于控制，每次都从上一次找到的元素的下一个位置开始截取字符串
                    continue;
                if(dict.find(s.substr(j,i-j))!=dict.end())//从位置j开始，截取i-j长度的字符串，如果没有找到，那么将返回最后一个元素的后一个位置的迭代器
                {
                    isWordBreak[i]=true;
                    break;
                }
            }
        }
        return isWordBreak[len];
    }
};
