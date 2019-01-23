class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // frame size
        vector<int> mVec(26,0);

        for(auto &val:tasks) {
            mVec[val-'A']++;
        }
        sort(mVec.begin(),mVec.end());
        int i = 25;
        while(i>=0&&mVec[25]==mVec[i])i--;
        return max((mVec[25]-1)*(n+1)+25-i,static_cast<int>(tasks.size()));
    }
};
