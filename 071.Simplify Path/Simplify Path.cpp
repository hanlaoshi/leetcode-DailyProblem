class Solution {
public:
    static bool isSlash(char c)
    {
        return (c == '/');
    }
    static bool notSlash(char c)
    {
        return !isSlash(c);
    }
    vector<string> split(string str)
    {
        vector<string> ret;
        string::iterator it = str.begin();
        while(it != str.end())
        {
            it = find_if(it, str.end(), notSlash);
            string::iterator it2 = find_if(it, str.end(), isSlash);
            if(it != str.end())
                ret.push_back(string(it, it2));
            it = it2;
        }
        return ret;
    }
    string simplifyPath(string path) {
        vector<string> v = split(path);
        stack<string> stk;
        string ret = "";
        for(int i = 0; i < v.size(); i ++)
        {
            if(v[i] == ".")
                ;
            else if(v[i] == "..")
            {
                if(!stk.empty())
                    stk.pop();
            }
            else
                stk.push(v[i]);
        }
        while(!stk.empty())
        {
            ret = "/" + stk.top() + ret;
            stk.pop();
        }
        if(ret == "")
            return "/";
        return ret;
    }
};