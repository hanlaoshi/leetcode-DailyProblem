解分为三步：

(1)构造两级向量(vector<vector<int> > v)

链式存放前一个字符的位置。

(2)基于向量v逆向递归寻找词，借助栈

[dog　　-->　　[dog, sand　　-->　　[dog, sand, cat

                 　　[dog, and　　 -->　　[dog, and, cats

(3)出栈时词以空格隔开，存入ret向量

"cat sand dog"

"cats and dog"
class Solution {
public:
    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
        vector<string> ret;
        string news = "0" + s;
        int n = news.size();
        vector<vector<int> > v(n);
        vector<bool> bpos(n, false);
        bpos[0] = true;
        for(int i = 1; i < n; i ++)
        {
            for(int j = 0; j < i; j ++)
            {
                if(bpos[j] == true && wordDict.find(news.substr(j+1, i-j)) != wordDict.end())
                {
                    bpos[i] = true;
                    v[i].push_back(j);   
                }
            }
        }
        if(bpos[n-1] == false)
            return ret;
        else
        {
            stack<string> stk;
            genRet(ret, news, v, stk, n-1);
            return ret;
        }
    }
    void genRet(vector<string>& ret, string news, vector<vector<int> > v, stack<string> stk, int bpos)
    {
        if(bpos == 0)
        {// generate final string
            string str;
            while(!stk.empty())
            {
                string top = stk.top();
                stk.pop();
                str += (top + " ");
            }
            str.erase(str.end()-1);
            ret.push_back(str);
        }
        else
        {
            for(int i = 0; i < v[bpos].size(); i ++)
            {
                string cur = news.substr(v[bpos][i]+1, bpos-v[bpos][i]);
                stk.push(cur);
                genRet(ret, news, v, stk, v[bpos][i]);
                stk.pop();
            }
        }
    }
};