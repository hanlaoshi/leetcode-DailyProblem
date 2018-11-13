
public List<List<Integer>> combinationSum2(int[] candidates, int target) {
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		List<Integer> tmp = new ArrayList<>();
		// 此题必须先排序
		Arrays.sort(candidates);
		dfsCore(res, 0, 0, tmp, candidates, target);
		return res;
	}
 
	private void dfsCore(List<List<Integer>> res, int curIdx, int sum, List<Integer> tmp, int[] candidates,
 
			int target) {
 
		if (sum > target)
			return;
		if (sum == target) {
			res.add(new ArrayList<Integer>(tmp));
			return;
		}
		//i = curIdx往后走，避免重复
		for (int i = curIdx; i < candidates.length; i++) {
			// 如果此层，下一个数跟当前数相等，则直接跳过，
			if (i > curIdx && candidates[i] == candidates[i - 1])
																	
				continue;
			// 剪枝，可以没有，目的为了优化，必须先排序
			if (target < candidates[i])
				return;
			sum += candidates[i];
			// 剪枝，可以没有，目的为了优化，必须先排序
			if (target < sum)
				return;
 
			tmp.add(candidates[i]);
			// 传入i+1
			dfsCore(res, i + 1, sum, tmp, candidates, target);
			tmp.remove(tmp.size() - 1);
			// 回溯
			sum -= candidates[i];
		}
	}
