'''
采用回溯法。由于组合中的数字要按序排列，我们先将集合中的数排序。依次把数字放入组合中，
因为所有数都是正数，如果当前和已经超出目标值，则放弃；如果和为目标值，则加入结果集；
如果和小于目标值，则继续增加元素。
由于结果集中不允许出现重复的组合，所以增加元素时只增加当前元素及之后的元素。
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates, target, [], result)
        return result

    def combination(self, candidates, target, current, result):
        s = sum(current) if current else 0
        if s > target:
            return
        elif s == target:
            result.append(current)
            return
        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, current + [v], result)


if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
