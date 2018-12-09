/*
朴素的判断必定超时，我们每次判断一个数是素数的时候，就将它的倍数标记为非素数即可。
*/

class Solution {
public:
	int countPrimes(int n) {
		if (n <= 2) return 0;
		bool * isPrimer = new bool[n];
		for (int i = 0; i < n; i++)	isPrimer[i] = true;
		for (int i = 2; i * i < n; i++) {
			if (isPrimer[i])
				for (int j = i ; j * i < n; j ++)
					isPrimer[j * i] = false;
		}
		int res = 0;
		for (int i = 2; i < n; i++)
			if (isPrimer[i]) res++;
		delete[] isPrimer;
		return res;
	}
};
