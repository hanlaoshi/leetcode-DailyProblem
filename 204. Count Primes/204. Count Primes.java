/*
使用见埃拉托色尼筛法。

（1）先把1删除（现今数学界1既不是质数也不是合数）

　　（2）读取队列中当前最小的数2，然后把2的倍数删去

　　（3）读取队列中当前最小的数3，然后把3的倍数删去

　　（4）读取队列中当前最小的数5，然后把5的倍数删去

　　（5）如上所述直到需求的范围内所有的数均删除或读取
  
*/
  
public int countPrimes(int n) {
		if (n <= 1) {
			return 0;
		}
		// 默认所有的元素值都会设置为false，boolean初始值为false
		boolean[] notPrime = new boolean[n];
		notPrime[0] = true;
		notPrime[1] = true;
		for (int i = 2; i * i < n; i++) {
			if (!notPrime[i]) {
				// 如果i是一个质数， 将i的倍数设置为非质数,
				//j += i相当于i的3倍，4倍……
				for (int j = 2 * i; j < n; j += i) {
					notPrime[j] = true;
				}
			}
		}
		// 统计质数的个数
		int result = 0;
		for (boolean notPri : notPrime) {
			if (!notPri) {
				result++;
			}
		}
		return result;
	}
  
