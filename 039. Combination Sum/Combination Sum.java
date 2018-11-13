//采用深度优先搜索的思想+回溯(可以不排序，并去掉剪枝)

	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		List<Integer> tmp = new ArrayList<>();
		// 排序可以避免重复，结果可以按照顺序输出
		Arrays.sort(candidates);
		dfsCore(res, 0, 0, tmp, candidates, target);
		return res;
	}
 
	private void dfsCore(List<List<Integer>> res, 
			int curIdx, int sum, List<Integer> tmp, int[] candidates,
			int target) {
		if (sum > target)
			return;
		if (sum == target) {
			res.add(new ArrayList<Integer>(tmp));
			return;
		}
		for (int i = curIdx; i < candidates.length; i++) {
			// 剪枝，可以没有，目的为了优化，必须先排序
			if (target < candidates[i])
				return;
			sum += candidates[i];
			// 剪枝，可以没有，目的为了优化，必须先排序
			if (target < sum)
				return;
 
			tmp.add(candidates[i]);
			// 之所以不传i+1的原因是：
			// The same repeated number may be
			// chosen from C unlimited number of time
			dfsCore(res, i, sum, tmp, candidates, target);
			tmp.remove(tmp.size() - 1);
			// 回溯
			sum -= candidates[i];
		}
	}
