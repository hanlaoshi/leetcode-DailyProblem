
class Solution {
public:
	int strStr(string haystack, string needle) {
		const int n = needle.size();
		const int m = haystack.size();
		int *next = new int[n];
		getNext(needle, next);
		int i = 0;
		int j = 0;
		while (i < m && j < n){  //此处使用needle.size()会出问题。
			if (j==-1 || haystack[i] == needle[j]){
				i++; 
				j++;
			}
			else
				j = next[j];
		}
		if (j == n) return i - j;
		else 
			return -1;
	}
	void getNext(string & needle, int next[]){
		int n = needle.size();
		int k = -1;
		int j = 0;
		next[0] = -1;
		while (j < n - 1){
			if (k == -1 || needle[j] == needle[k]){
				j++;
				k++;
				next[j] = k;
			}
			else
				k = next[k];
		}
	}
};
