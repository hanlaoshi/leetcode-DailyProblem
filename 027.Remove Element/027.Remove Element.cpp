//----------cpp------------
class Solution {
	public:
		int removeElement(vector<int>& nums, int val) {
			int n = nums.size(), p = 0;
			for (int i = 0; i < n; i++) {
				if (val != nums[i])
					nums[p++] = nums[i];
			}
			return p;
		}
};
