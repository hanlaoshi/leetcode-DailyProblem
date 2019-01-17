/*
解题思路：

解法一：暴力解法，遍历nums1，对其中的每个数，在nums2中找到该数，然后在nums2中该数的右边找第一个较大的数。
*/


public int[] nextGreaterElement(int[] findNums, int[] nums) {
		int findLen = findNums.length;
		int numsLen = nums.length;
		int i, j, k;
		int[] res = new int[findLen];
		for (i = 0; i < findLen; i++) {
			for (j = 0; j < numsLen; j++) {
				if (findNums[i] == nums[j]) {
					for (k = j + 1; k < numsLen; k++) {
						if (nums[k] > findNums[i]) {
							res[i] = nums[k];
							break;
						}
					}
					if (k == numsLen)
						res[i] = -1;
					break;
				}
			}
		}
		return res;
	}


/* 
解法二：首先确定nums2中每一个数和右边第一个较大数的关系。方法为维护一个栈和一个map，从尾到头遍历nums2，对于每一个数，
如果栈顶元素小于该数，则栈顶元素出栈，直到找到大于该数的栈顶元素，此时将<该数，栈顶元素>放入map中，然后将该数也入栈；如果栈空了，
则将<该数，-1>放入map中，同样将该数入栈。确定好这样一个关系后，就可以直接遍历nums1，对每一个元素直接在map中执行get，
就可以确定nums2中下一个较大元素的值了。

*/

public int[] nextGreaterElement(int[] findNums, int[] nums) {
        int findLen = findNums.length;
		int numsLen = nums.length;
		int[] res = new int[findLen];
		if (findLen == 0 || numsLen == 0 || findLen > numsLen)
			return res;
		Map<Integer, Integer> map = new HashMap<>();
		int[] stack = new int[numsLen];
		int index = -1;
		int i, j;
		int curMax = nums[numsLen - 1];
		map.put(curMax, -1);
		for (i = numsLen - 1; i >= 0; i--) {
			while (index >= 0) {
				if (nums[i] > stack[index])
					--index;
				else {
					map.put(nums[i], stack[index]);
					stack[++index] = nums[i];
					break;
				}
			}
			if (index < 0) {
				map.put(nums[i], -1);
				stack[++index] = nums[i];
			}
		}
		for (j = 0; j < findLen; j++) {
			res[j] = map.get(findNums[j]);
		}
		return res;
    }


//方法三  多年未见大佬
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        map<int, int> mp;
        int cc = 1;
        int n = findNums.size(), m = nums.size();
        for (int i = 0; i < n; i++) {
            mp[findNums[i]] = cc++;
        }
        vector<int> ans(n, -1);
        stack<int> s;
        for (int i = 0; i < m; i++) {
            while (!s.empty() && nums[s.top()] < nums[i]) {
                int tmp = mp[nums[s.top()]];
                if (tmp) ans[tmp - 1] = nums[i];
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) s.pop();
        return ans;
    }
};
