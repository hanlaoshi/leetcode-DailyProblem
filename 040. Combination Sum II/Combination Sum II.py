'''
这道题和 Combination Sum 极其相似，主要的区别是Combination Sum中的元素是没有重复的，
且每个元素可以使用无限次；而这题中的元素是有重复的，每个元素最多只能使用一次。
最开始的想法是加下一个元素时不要考虑当前元素，
且把结果用集合存储以防止重复的组合出现，但结果超时了。
改用手动把所有与当前元素相等的元素都去掉即可。
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
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
            i = 0
            while i < len(candidates):
                self.combination(candidates[i + 1:], target, current + [candidates[i]], result)
                # ignore repeating elements
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1


if __name__ == "__main__":
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) 
