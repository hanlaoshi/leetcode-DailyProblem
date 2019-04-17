//从后向前考虑。如果A中的先遍历完，应把B中剩下的元素复制到A中。

public void merge(int[] nums1, int m, int[] nums2, int n) {
		int index = m + n - 1;
		int i = m - 1;
		int j = n - 1;
		while (i >= 0 && j >= 0)
			if (nums1[i] >= nums2[j]) {
				nums1[index] = nums1[i];
				i--;
				index--;
			} else {
				nums1[index] = nums2[j];
				j--;
				index--;
			}
		//继续遍历剩下的元素
		if (i == -1) {
			while (j >= 0) {
				nums1[index] = nums2[j];
				j--;
				index--;
			}
		}
	}

