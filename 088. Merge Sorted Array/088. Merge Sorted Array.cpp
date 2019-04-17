//把数组依次从后往前放可以减少大量的数据移动。

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        nums1.resize(m+n);
        int p1 = m-1;
        int p2 = n-1;
        int tmp = m+n-1;
        while(p1+1&&p2+1){
            if(nums1[p1]>nums2[p2]){
                nums1[tmp--] = nums1[p1--];
            }else{
                nums1[tmp--] = nums2[p2--];
            }
        }
        if(p2+1)
            while(p2+1){
                nums1[p2] = nums2[p2];
                p2--;
            }
    }
};
