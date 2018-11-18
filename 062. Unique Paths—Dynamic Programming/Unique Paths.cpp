/*

这道题是求全排列问题，给的输入数组没有重复项，
这跟之前的那道 Combinations 组合项 和类似，解法基本相同，
但是不同点在于那道不同的数字顺序只算一种，是一道典型的组合题，
而此题是求全排列问题，还是用递归DFS来求解。
这里我们需要用到一个visited数组来标记某个数字是否访问过，
然后在DFS递归函数从的循环应从头开始，而不是从level开始，
这是和 Combinations 组合项 不同的地方，其余思路大体相同

*/

class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> > res;
        vector<int> out;
        vector<int> visited(num.size(), 0);
        permuteDFS(num, 0, visited, out, res);
        return res;
    }
    void permuteDFS(vector<int> &num, int level, vector<int> &visited, vector<int> &out, vector<vector<int> > &res) {
        if (level == num.size()) res.push_back(out);
        else {
            for (int i = 0; i < num.size(); ++i) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    out.push_back(num[i]);
                    permuteDFS(num, level + 1, visited, out, res);
                    out.pop_back();
                    visited[i] = 0;
                }
            }
        }
    }
};


/*
//还有一种递归的写法，更简单一些，这里是每次交换num里面的两个数字，经过递归可以生成所有的排列情况

class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> > res;
        permuteDFS(num, 0, res);
        return res;
    }
    void permuteDFS(vector<int> &num, int start, vector<vector<int> > &res) {
        if (start >= num.size()) res.push_back(num);
        for (int i = start; i < num.size(); ++i) {
            swap(num[start], num[i]);
            permuteDFS(num, start + 1, res);
            swap(num[start], num[i]);
        }
    }
};
*/


/*
//最后再来看一种方法，这种方法是CareerCup书上的方法，也挺不错的，这道题是思想是这样的：

//当n=1时，数组中只有一个数a1，其全排列只有一种，即为a1

//当n=2时，数组中此时有a1a2，其全排列有两种，a1a2和a2a1，那么此时我们考虑和上面那种情况的关系，
//我们发现，其实就是在a1的前后两个位置分别加入了a2

//当n=3时，数组中有a1a2a3，此时全排列有六种，分别为a1a2a3, a1a3a2, a2a1a3, a2a3a1, a3a1a2, 和 a3a2a1。
//那么根据上面的结论，实际上是在a1a2和a2a1的基础上在不同的位置上加入a3而得到的。

//_ a1 _ a2 _ : a3a1a2, a1a3a2, a1a2a3

//_ a2 _ a1 _ : a3a2a1, a2a3a1, a2a1a3

class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        if (num.empty()) return vector<vector<int> >(1, vector<int>());
        vector<vector<int> > res;
        int first = num[0];
        num.erase(num.begin());
        vector<vector<int> > words = permute(num);
        for (auto &a : words) {
            for (int i = 0; i <= a.size(); ++i) {
                a.insert(a.begin() + i, first);
                res.push_back(a);
                a.erase(a.begin() + i);
            }
        }   
        return res;
    }
};
*/





